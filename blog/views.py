import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.shortcuts import get_object_or_404


# Create your views here.
def article(request):
    return HttpResponse("sai ram")


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return Response({"msg": "List of articles", "data": [{"title": i.title} for i in articles]})

    def post(self, request):
        data = json.loads(request.body)
        article = Article.objects.create(**data)
        return Response({"msg": "article created successfully", "data": {"id": article.id, "title": article.title}})


class ArticleDetail(APIView):
    def get(self, request, article):
        object = get_object_or_404(Article, id=article)
        return Response({"msg": "details of article", "data": {"id": object.id, "title": object.title}})

    def put(self, request, article):
        data = json.loads(request.body)
        object = get_object_or_404(Article, id=article)
        object.title = data["title"]
        object.save()
        return Response({"msg": "article updated successfully", "data": {"id": object.id, "title": object.title}})

    def delete(self, request, article):
        object = get_object_or_404(Article, id=article)
        object.delete()
        return Response({"msg": "article deleted successfully", "data": {}})
