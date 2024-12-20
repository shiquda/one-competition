# backend/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', '普通用户'),
        ('admin', '管理员'),
    )
    email  = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular', verbose_name="用户类型")
    
    # 使用createsuperuser创建的用户默认是管理员类型
    def save(self, *args, **kwargs):
        # 如果是新创建的用户且是超级用户，则设置为管理员类型
        if self.is_superuser:
            self.user_type = 'admin'
        super().save(*args, **kwargs)
    def is_admin_user(self):
        return self.user_type == 'admin'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Competition(models.Model):
    # 增加一个字段，用于记录竞赛的审核状态
    REVIEW_STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '审核通过'),
        ('rejected', '审核拒绝'),
    )

    name = models.CharField(max_length=255, verbose_name="竞赛名称")
    types = models.JSONField(default=list, verbose_name="竞赛类型")  # 竞赛类型列表
    levels = models.JSONField(default=list, verbose_name="竞赛级别")  # 竞赛级别列表
    description = models.TextField(verbose_name="简介")
    website = models.URLField(verbose_name="竞赛官网")
    other_info = models.TextField(verbose_name="其他信息", blank=True, null=True)
    review_status = models.CharField(
        max_length=20,
        choices=REVIEW_STATUS_CHOICES,
        default='pending',
        verbose_name="审核状态"
    )    

    def __str__(self):
        return self.name


class CompetitionTimeline(models.Model):
    # 使用外键链接到 Competition 模型，可以为每个竞赛添加多个时间节点（如开始和结束时间等）
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="timeline")
    node_name = models.CharField(max_length=100, verbose_name="节点名称")
    date = models.DateField(verbose_name="日期")
   

    def __str__(self):
        return f"{self.competition.name} - {self.node_name}"
