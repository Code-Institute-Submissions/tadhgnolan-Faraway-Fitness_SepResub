from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_articles, name='news'),
    path('article/<int:id>/', views.view_article, name='view_article'),
    path('articles/add/', views.add_article, name='add_article'),
    path('article/delete/<int:id>/', views.delete_article, name='delete_article'),
    path('article/update/<int:id>/', views.update_article, name='update_article'),
]
