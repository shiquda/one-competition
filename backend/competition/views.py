# backend/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Competition, CompetitionTimeline
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Competition, CompetitionTimeline, User
from functools import wraps
from .serializers import CompetitionSerializer  # 需要创建这个序列化器


def admin_required(view_func):
    """管理员权限验证装饰器"""
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "请先登录"}, status=status.HTTP_401_UNAUTHORIZED)
        if not request.user.is_admin_user():
            return Response({"error": "需要管理员权限"}, status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return wrapped_view

# 获取所有审核通过的竞赛信息


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_competitions(request):
    # 只获取审核通过的竞赛
    competitions = Competition.objects.filter(review_status='approved').values()

    # 添加时间节点信息
    for competition in competitions:
        timelines = CompetitionTimeline.objects.filter(
            competition_id=competition['id']
        ).values('node_name', 'date')
        competition['timeline'] = list(timelines)

    return JsonResponse(list(competitions), safe=False)

# 获取单个竞赛（审核通过）的详细信息


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_competition_detail(request, competition_id):
    # 获取并检查竞赛是否审核通过
    competition = get_object_or_404(Competition, pk=competition_id)

    if competition.review_status != 'approved':
        return Response(
            {'error': '该竞赛尚未通过审核或已被拒绝'},
            status=status.HTTP_403_FORBIDDEN
        )

    # 获取时间节点信息
    timelines = competition.timeline.all().values()

    data = {
        "id": competition.id,
        "name": competition.name,
        "types": competition.types,
        "levels": competition.levels,
        "description": competition.description,
        "website": competition.website,
        "other_info": competition.other_info,
        "timeline": list(timelines),
    }

    return JsonResponse(data)

# 添加新竞赛


@csrf_exempt
@api_view(['POST'])
@admin_required
def add_competition(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': '无效的JSON数据'}, status=400)

    # 必要字段
    required_fields = ['name', 'types', 'levels', 'description', 'website', 'timeline']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return JsonResponse({'error': f'缺少字段: {", ".join(missing_fields)}'}, status=400)

    name = data.get('name')
    types = data.get('types')
    levels = data.get('levels')
    description = data.get('description')
    website = data.get('website')
    timeline = data.get('timeline')
    other_info = data.get('other_info', '')

    # 验证字段类型
    if not isinstance(name, str) or not name.strip():
        return JsonResponse({'error': '竞赛名称必须是非空字符串'}, status=400)

    if not isinstance(types, list) or not all(isinstance(t, str) and t.strip() for t in types):
        return JsonResponse({'error': '竞赛类型必须是非空字符串数组'}, status=400)

    if not isinstance(levels, list) or not all(isinstance(l, str) and l.strip() for l in levels):
        return JsonResponse({'error': '竞赛级别必须是非空字符串数组'}, status=400)

    if not isinstance(description, str) or not description.strip():
        return JsonResponse({'error': '竞赛描述必须是非空字符串'}, status=400)

    if not isinstance(timeline, dict):
        return JsonResponse({'error': '时间节点必须是一个对象'}, status=400)

    # 验证 timeline 包含 start_time 和 end_time
    required_timeline_fields = ['start_time', 'end_time']
    missing_timeline_fields = [field for field in required_timeline_fields if field not in timeline]

    if missing_timeline_fields:
        return JsonResponse({'error': f'时间节点缺少字段: {", ".join(missing_timeline_fields)}'}, status=400)

    start_time = timeline.get('start_time')
    end_time = timeline.get('end_time')

    # 验证时间格式
    date_format = "%Y-%m-%d"
    try:
        start_date = datetime.strptime(start_time, date_format).date()
    except (ValueError, TypeError):
        return JsonResponse({'error': 'start_time 必须是有效的日期，格式为 YYYY-MM-DD'}, status=400)

    try:
        end_date = datetime.strptime(end_time, date_format).date()
    except (ValueError, TypeError):
        return JsonResponse({'error': 'end_time 必须是有效的日期，格式为 YYYY-MM-DD'}, status=400)

    if start_date > end_date:
        return JsonResponse({'error': 'start_time 不能晚于 end_time'}, status=400)

    # 验证URL
    url_validator = URLValidator()
    try:
        url_validator(website)
    except ValidationError:
        return JsonResponse({'error': '竞赛官网必须是一个有效的URL'}, status=400)

    if other_info and not isinstance(other_info, str):
        return JsonResponse({'error': '其他信息必须是字符串'}, status=400)

    try:
        competition = Competition.objects.create(
            name=name.strip(),
            types=[t.strip() for t in types],
            levels=[l.strip() for l in levels],
            description=description.strip(),
            website=website.strip(),
            other_info=other_info.strip() if other_info else ''
        )

        # 创建时间节点
        CompetitionTimeline.objects.create(
            competition=competition,
            node_name='start_time',
            date=start_date
        )
        CompetitionTimeline.objects.create(
            competition=competition,
            node_name='end_time',
            date=end_date
        )
    except Exception as e:
        return JsonResponse({'error': '创建竞赛时发生服务器错误'}, status=500)

    return JsonResponse({'message': '竞赛创建成功', 'id': competition.id}, status=201)

# 删除竞赛


@admin_required
def delete_competition(request, competition_id):
    try:
        competition = get_object_or_404(Competition, pk=competition_id)
        competition.delete()
        return JsonResponse({'message': '竞赛删除成功'})
    except Competition.DoesNotExist:
        return JsonResponse({'error': '找不到指定的竞赛'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'删除竞赛时发生服务器错误: {e}'}, status=500)


def admin_required(view_func):
    """管理员权限验证装饰器"""
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "请先登录"}, status=status.HTTP_401_UNAUTHORIZED)
        if not request.user.is_admin_user():
            return Response({"error": "需要管理员权限"}, status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return wrapped_view


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """用户注册"""
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response({"error": "用户名和密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "用户名已存在"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            user_type='regular'  # 默认创建普通用户
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': '注册成功',
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'username': user.username,
            'user_type': user.user_type
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """用户登录"""
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "用户名和密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': '登录成功',
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'username': user.username,
            'user_type': user.user_type
        })
    return Response({"error": "用户名或密码错误"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """用户修改密码"""
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    if not old_password or not new_password or not confirm_password:
        return Response({"error": "旧密码、新密码和确认密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(old_password):
        return Response({"error": "旧密码不正确"}, status=status.HTTP_400_BAD_REQUEST)

    if new_password != confirm_password:
        return Response({"error": "新密码和确认密码不匹配"}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()
    return Response({"message": "密码修改成功"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_competitions_admin(request):
    # 检查用户是否是管理员
    if not request.user.is_admin_user():
        return Response({
            'error': '权限不足，仅管理员可访问此接口'
        }, status=status.HTTP_403_FORBIDDEN)

    # 如果是管理员，获取所有竞赛
    competitions = Competition.objects.all()
    serializer = CompetitionSerializer(competitions, many=True)
    data = serializer.data  # 这是一个字典列表

    # 为每个竞赛添加时间节点信息
    for competition in data:
        timelines = CompetitionTimeline.objects.filter(
            competition_id=competition['id']
        ).values('node_name', 'date')
        competition['timeline'] = list(timelines)

    return Response(data)


@api_view(['PUT'])
@admin_required
def update_competition(request, competition_id):
    try:
        # 获取竞赛对象
        competition = get_object_or_404(Competition, pk=competition_id)

        # 获取请求数据
        data = request.data

        # 更新基本字段（如果提供）
        if 'name' in data:
            competition.name = data['name'].strip()
        if 'types' in data and isinstance(data['types'], list):
            competition.types = [t.strip() for t in data['types']]
        if 'levels' in data and isinstance(data['levels'], list):
            competition.levels = [l.strip() for l in data['levels']]
        if 'description' in data:
            competition.description = data['description'].strip()
        if 'website' in data:
            # 验证 URL
            url_validator = URLValidator()
            try:
                url_validator(data['website'])
                competition.website = data['website'].strip()
            except ValidationError:
                return Response({'error': '无效的URL格式'}, status=status.HTTP_400_BAD_REQUEST)
        if 'other_info' in data:
            competition.other_info = data['other_info'].strip()
        if 'review_status' in data:
            if data['review_status'] in dict(Competition.REVIEW_STATUS_CHOICES):
                competition.review_status = data['review_status']
            else:
                return Response({'error': '无效的审核状态'}, status=status.HTTP_400_BAD_REQUEST)

        # 更新时间节点（如果提供）
        if 'timeline' in data:
            timeline = data['timeline']
            date_format = "%Y-%m-%d"

            if 'start_time' in timeline:
                try:
                    start_date = datetime.strptime(timeline['start_time'], date_format).date()
                    start_timeline = competition.timeline.filter(node_name='start_time').first()
                    if start_timeline:
                        start_timeline.date = start_date
                        start_timeline.save()
                except (ValueError, TypeError):
                    return Response({'error': 'start_time 必须是有效的日期，格式为 YYYY-MM-DD'},
                                    status=status.HTTP_400_BAD_REQUEST)

            if 'end_time' in timeline:
                try:
                    end_date = datetime.strptime(timeline['end_time'], date_format).date()
                    end_timeline = competition.timeline.filter(node_name='end_time').first()
                    if end_timeline:
                        end_timeline.date = end_date
                        end_timeline.save()
                except (ValueError, TypeError):
                    return Response({'error': 'end_time 必须是有效的日期，格式为 YYYY-MM-DD'},
                                    status=status.HTTP_400_BAD_REQUEST)

        # 保存更新
        competition.save()

        # 返回更新后的竞赛信息
        serializer = CompetitionSerializer(competition)
        return Response({
            'message': '竞赛信息更新成功',
            'data': serializer.data
        })

    except Competition.DoesNotExist:
        return Response({'error': '找不到指定的竞赛'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f'更新竞赛时发生错误: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_competition(request):
    try:
        data = request.data

        # 必要字段检查
        required_fields = ['name', 'types', 'levels', 'description', 'website', 'timeline']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return Response({'error': f'缺少字段: {", ".join(missing_fields)}'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 基础数据验证
        if not isinstance(data['types'], list) or not data['types']:
            return Response({'error': '竞赛类型必须是非空数组'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(data['levels'], list) or not data['levels']:
            return Response({'error': '竞赛级别必须是非空数组'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 验证时间节点
        timeline = data.get('timeline')
        if not isinstance(timeline, dict) or 'start_time' not in timeline or 'end_time' not in timeline:
            return Response({'error': '时间节点格式不正确'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 验证并转换日期
        date_format = "%Y-%m-%d"
        try:
            start_date = datetime.strptime(timeline['start_time'], date_format).date()
            end_date = datetime.strptime(timeline['end_time'], date_format).date()
        except (ValueError, TypeError):
            return Response({'error': '日期格式必须为 YYYY-MM-DD'},
                            status=status.HTTP_400_BAD_REQUEST)

        if start_date > end_date:
            return Response({'error': '开始时间不能晚于结束时间'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 验证URL
        url_validator = URLValidator()
        try:
            url_validator(data['website'])
        except ValidationError:
            return Response({'error': '无效的URL格式'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 创建竞赛记录，设置为待审核状态
        competition = Competition.objects.create(
            name=data['name'].strip(),
            types=[t.strip() for t in data['types']],
            levels=[l.strip() for l in data['levels']],
            description=data['description'].strip(),
            website=data['website'].strip(),
            other_info=data.get('other_info', '').strip(),
            review_status='pending'  # 设置为待审核状态
        )

        # 创建时间节点
        CompetitionTimeline.objects.create(
            competition=competition,
            node_name='start_time',
            date=start_date
        )
        CompetitionTimeline.objects.create(
            competition=competition,
            node_name='end_time',
            date=end_date
        )

        return Response({
            'message': '竞赛投稿成功，等待管理员审核',
            'competition_id': competition.id
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'投稿失败: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
