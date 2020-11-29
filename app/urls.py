from django.urls import path
from . import views
from .views import IndexView,StorysView

app_name = 'app'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('storys/',StorysView.as_view(),name='storys'),
]