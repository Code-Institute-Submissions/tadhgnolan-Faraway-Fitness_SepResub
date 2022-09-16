from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_articles, name='news'),
    path('article/<int:id>/', views.view_article, name='view_article')
]
