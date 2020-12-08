from django.shortcuts import render,redirect
from django.views import generic,View
from .models import MainTask,SubTask
from django.http.response import HttpResponse
import json


# ストーリーの達成率を返す関数
def get_story_achievement_rate():
    storys = MainTask.objects.filter(types=1)
    task_count = 0
    fin_task_count = 0
    for story in storys:
        task_count += story.subtask_set.all().count()
        fin_task_count += story.subtask_set.filter(condition=3).count()
    achievement_rate = round(( fin_task_count / task_count ) * 100,1)
    return achievement_rate


# トップ画面はないのでストーリー一覧に飛ばす
class IndexView(generic.RedirectView):
    url = '/storys/'


# ストーリー画面のView
class StorysView(generic.ListView):
    template_name = "app/storys.html"
    model = MainTask
    context_object_name = "storys"

    # メインストーリーの情報だけ取得
    def get_queryset(self):
        # メインストーリーのデータだけ取得
        return MainTask.objects.filter(types=1)

    # ストーリー全体での達成率もセットする
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['achievement_rate'] = get_story_achievement_rate()
        return context



# タスクの状態を変更して完了メッセージを返す(Ajaxでアクセスされる想定)
class SubTaskConditionChangeView(View):
    def get(self,request,*args,**kwargs):
        task_id = request.GET.get('task_id')
        condition = request.GET.get('condition')
        SubTask.objects.get(pk=task_id).setConditionChange(condition)
        data = {
            'success':'success',
            'achievement_rate':get_story_achievement_rate(),
        }
        # 辞書からjson形式にシリアライズ
        data_json = json.dumps(data)
        return HttpResponse(data_json,content_type='application/json')




