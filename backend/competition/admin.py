# backend/competition/admin.py
from django import forms
from django.contrib import admin
from .models import Competition, CompetitionTimeline, User


class CompetitionAdminForm(forms.ModelForm):
    types = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '输入竞赛类型，用逗号分隔'}),
        required=False,
        help_text="使用逗号分隔类型，例如 '计算机, 数学'"
    )
    levels = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '输入竞赛级别，用逗号分隔'}),
        required=False,
        help_text="使用逗号分隔级别，例如 '国家级, 省级'"
    )

    class Meta:
        model = Competition
        fields = '__all__'

    def clean_types(self):
        types = self.cleaned_data.get('types', '')
        return [type.strip() for type in types.split(',') if type.strip()]

    def clean_levels(self):
        levels = self.cleaned_data.get('levels', '')
        return [level.strip() for level in levels.split(',') if level.strip()]


class CompetitionTimelineInline(admin.TabularInline):
    model = CompetitionTimeline
    extra = 1  # 显示一个额外的空白表单，用于添加新节点
    fields = ('node_name', 'date')
    verbose_name = "时间节点"
    verbose_name_plural = "时间节点"


class CompetitionAdmin(admin.ModelAdmin):
    form = CompetitionAdminForm
    list_display = ('name', 'display_types', 'display_levels', 'get_start_time', 'get_end_time')
    search_fields = ('name',)
    inlines = [CompetitionTimelineInline]

    def display_types(self, obj):
        return ', '.join(obj.types)
    display_types.short_description = "竞赛类型"

    def display_levels(self, obj):
        return ', '.join(obj.levels)
    display_levels.short_description = "竞赛级别"

    def get_start_time(self, obj):
        timeline = obj.timeline.all().order_by('date')
        if timeline.exists():
            return timeline.first().date
        return '暂无'
    get_start_time.short_description = "开始时间"

    def get_end_time(self, obj):
        timeline = obj.timeline.all().order_by('-date')
        if timeline.exists():
            return timeline.first().date
        return '暂无'
    get_end_time.short_description = "结束时间"


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(User)
