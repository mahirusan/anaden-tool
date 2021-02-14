from django.urls import path
from . import views
from .views import IndexView,StorysView,SubTaskConditionChangeView,GaitensView

app_name = 'app'

urlpatterns = [
    path('',IndexView.as_view(),name='index'), #トップ画面処理(今のところストーリーにリダイレクトするだけ)
    path('storys/',StorysView.as_view(),name='storys'), #ストーリー画面
    path('subtask_update/',SubTaskConditionChangeView.as_view(),name="condition_change"), #Ajaxタスク状態変化処理
    path('gaitens/',GaitensView.as_view(),name='gaitens'), #外典クエスト画面
]