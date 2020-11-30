from django.urls import path
from . import views
from .views import IndexView,StorysView,SubTaskConditionChangeView

app_name = 'app'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('storys/',StorysView.as_view(),name='storys'),
    path('subtask_update/',SubTaskConditionChangeView.as_view(),name="condition_change"),
]