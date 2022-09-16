from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Topic
from .forms import ArticleForm, TopicForm

# Retrieves article information for display on news page
def get_articles(request):
    articles = Article.objects.all()
    template = "news/news.html"
    context = {
        "articles": articles,
    }
    return render(request, template, context)


# Renders full article details on article details page
def view_article(request, id):
    article = get_object_or_404(Article, id=id)
    template = "news/view_article.html"
    context = {
        "article": article,
    }
    return render(request, template, context)


# Checks if user is admin / superuser before allowing them to post
@login_required
def add_article(request):
    if not request.user.is_superuser:
        messages.error(request, "Invalid user permission")
        return redirect(reverse("news"))
    form = ArticleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Article added")
            return redirect(reverse("news"))
        messages.error(request, "Error. Please try again")

    template = "news/add_article.html"
    context = {
        "form": form,
    }
    return render(request, template, context)
