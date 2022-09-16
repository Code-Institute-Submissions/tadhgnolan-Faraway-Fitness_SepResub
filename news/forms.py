from django import forms
from .models import Article, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', )


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('headline', 'topic', 'content', )
