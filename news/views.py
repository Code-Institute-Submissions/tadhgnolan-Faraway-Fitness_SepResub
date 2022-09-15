from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Topic
from .forms import ArticleForm, TopicForm

# Retrieves article information for display on news page
def get_articles(request):
    articles = Article.objects.all()
    template = "news/articles.html"
    context = {
        "articles": articles,
    }
    return render(request, template, context)


# Renders full article details on article details page
def view_article(request, id):
    article = get_object_or_404(Article, id=id)
    template = "news/article_details.html"
    context = {
        "article": article,
    }
    return render(request, template, context)
