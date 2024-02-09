from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('category/<cat>/', views.source, name='source_news'),
    path('source/<cat>/<src>/', views.articles, name='articles'),
    path('q/<query>', views.search, name='search'),
    path('favorites/', views.favorites, name='favorites'),
    
]
