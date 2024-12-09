from rest_framework import serializers
from .models import Competition


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        # 或者指定具体字段: ['id', 'name', 'types', 'levels', 'description', 'website', 'other_info', 'review_status']
        fields = '__all__'
