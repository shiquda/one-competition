# backend/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Competition, CompetitionTimeline
import json

# 获取所有竞赛信息


def get_all_competitions(request):
    competitions = Competition.objects.all().values()
    # 加上时间节点信息
    for competition in competitions:
        competition['timeline'] = list(CompetitionTimeline.objects.filter(
            competition=competition['id']).values('node_name', 'date'))

    return JsonResponse(list(competitions), safe=False)

# 获取单个竞赛的详细信息


def get_competition_detail(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    timelines = competition.timeline.all().values()  # 获取时间节点信息
    data = {
        "id": competition.id,
        "name": competition.name,
        "type_labels": competition.type_labels,
        "level_labels": competition.level_labels,
        "description": competition.description,
        "website": competition.website,
        "other_info": competition.other_info,
        "timeline": list(timelines),
    }
    return JsonResponse(data)

# 添加新竞赛


def add_competition(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        competition = Competition.objects.create(
            name=data.get('name'),
            type_labels=data.get('type_labels'),
            level_labels=data.get('level_labels'),
            description=data.get('description'),
            website=data.get('website'),
            other_info=data.get('other_info', '')
        )
        return JsonResponse({'message': 'Competition created successfully', 'id': competition.id})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# 删除竞赛


def delete_competition(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    competition.delete()
    return JsonResponse({'message': 'Competition deleted successfully'})
