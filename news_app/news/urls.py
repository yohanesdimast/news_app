from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('sources/<cat>/', views.source, name='source_news'),
]
