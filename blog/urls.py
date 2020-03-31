from django.urls import path
from .views import ArticleList, ArticleDetail


urlpatterns = [
    path('article/', ArticleList.as_view(), name='article_list'),
    path('article/<str:article>/', ArticleDetail.as_view(), name='article_detail')
]