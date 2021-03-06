from django.urls import path
from . import views
from .views import IndexView,StorysView,SubTaskConditionChangeView,GaitensView,GaidensView,KaikousView,DansyosView,KyosousView

app_name = 'app'

urlpatterns = [
    path('',IndexView.as_view(),name='index'), #トップ画面処理(今のところストーリーにリダイレクトするだけ)
    path('storys/',StorysView.as_view(),name='storys'), #ストーリー画面
    path('subtask_update/',SubTaskConditionChangeView.as_view(),name="condition_change"), #Ajaxタスク状態変化処理
    path('gaitens/',GaitensView.as_view(),name='gaitens'), #外典クエスト画面
    path('gaidens/',GaidensView.as_view(),name='gaidens'), #外伝クエスト画面
    path('kaikous/',KaikousView.as_view(),name='kaikous'), #邂逅クエスト画面
    path('dansyos/',DansyosView.as_view(),name='dansyos'), #断章クエスト画面
    path('kyosous/',KyosousView.as_view(),name='kyosous'), #協奏クエスト画面
]