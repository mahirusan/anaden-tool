from django.shortcuts import render,redirect
from django.views import generic,View
from .models import MainTask,SubTask
from django.http.response import HttpResponse
import json

# イベント文字列に対するタイプ値を返す辞書
eventNumDict = {
    "story":1,
    "gaiten":2,
    "gaiden":3,
    "kaikou":4,
    "kyosou":5,
    "dansyo":6
}

# タイプの項目ごとの達成率を返す関数 return->項目ごとの達成率をセットした配列 ※storyのみ全体の達成率をそのまま返す
def get_main_achievement_rate(eventStr):
    # イベント番号に対するフィルターを掛け絞り込み
    main = MainTask.objects.filter(types=eventNumDict[eventStr])
    task_count = 0
    fin_task_count = 0
    if eventStr == "story":
        for task in main:
            task_count += task.subtask_set.all().count() # 全タスク数の取得
            fin_task_count += task.subtask_set.filter(condition=3).count() # 完了済みタスクの取得
        if task_count != 0:
            achievement_rate = round(( fin_task_count / task_count ) * 100,1) # 達成率の計算
            return achievement_rate
    else:
        achievementArray = [] #このリストに項目ごとの達成率を入れていく
        for task in main:
            task_count = task.subtask_set.all().count() # 全タスク数の取得
            fin_task_count = task.subtask_set.filter(condition=3).count() # 完了済みタスクの取得
            if task_count != 0:
                achievement_rate = round(( fin_task_count / task_count ) * 100,1) # 達成率の計算
            else:
                achievement_rate = 0
            achievementArray.append(achievement_rate) # 達成率を配列に退避
        return achievementArray
    



# タスクの状態を変更して完了メッセージを返す(Ajaxでアクセスされる想定)
class SubTaskConditionChangeView(View):
    def get(self,request,*args,**kwargs):
        task_id = request.GET.get('task_id') #subtaskのidの取得(採番数が増えるのでいずれ別の方法を検討すべき)
        condition = request.GET.get('condition') #現在のsubtaskの状態の取得
        req_type = request.GET.get('req_type') #リクエストタイプ(get_main_achievement_rateに繋げる)
        main_seq = request.GET.get('main_seq') #MainTaskのtypes(順序)、ない場合でもnoneを返す
        SubTask.objects.get(pk=task_id).setConditionChange(condition)
        if req_type == "story":
            achievement_rate = get_main_achievement_rate(req_type) #達成率の取得
        else:
            achievementArray = get_main_achievement_rate(req_type) #達成率リストを取得しカンマ区切りで連結
            achievement_rate = achievementArray[int(main_seq) - 1] #渡されたメインタスクの順序に合わせた達成率を取得

        data = {
            'success':'success',
            'achievement_rate':achievement_rate,
            'req_type':req_type,
            'main_seq':main_seq
        }
        
        # 辞書からjson形式にシリアライズ
        data_json = json.dumps(data)
        return HttpResponse(data_json,content_type='application/json')


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
        context['achievement_rate'] = get_main_achievement_rate("story")
        return context


# 外典クエスト画面のView
class GaitensView(generic.ListView):
    template_name = "app/gaiten.html"
    model = MainTask
    context_object_name = "gaitens"

    # 外典クエストの情報だけ取得
    def get_queryset(self):
        #外典クエストのデータだけ取得
        return MainTask.objects.filter(types=2)

    # 外典の達成率もそれぞれ取得しセット(外典ごとに取得)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['achievement_rates'] = get_main_achievement_rate("gaiten")
        return context