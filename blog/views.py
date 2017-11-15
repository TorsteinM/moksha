from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import Article
from .forms import ArticleForm


class BlogHomeListView(generic.ListView):
    template_name = "blog/article_home.html"
    model = Article


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "blog/article.html", context={'article': article})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                curr_user = User.objects.get(username=request.user.username)
            except User.DoesNotExist:
                curr_user = User.objects.get(username='admin')

            instance = form.save(commit=False)
            instance.author = curr_user
            instance.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())
    else:
        form = ArticleForm()

    return render(request, "blog/article_create.html", context={'form': form})


def article_delete(request, pk):
    success_url = reverse_lazy('blog:blog-home')
    article = Article.objects.get(id=pk)

    if request.method == "POST" and "delete" in request.POST:
        article.delete()
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponseRedirect(article.get_absolute_url())


def article_update(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            try:
                user = User.objects.get(username=request.user.username)
            except User.DoesNotExist:
                user = User.objects.get(username='admin')
            instance = form.save(commit=False)
            instance.author = user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ArticleForm(instance=article)

    return render(request, "blog/article_update.html", context={'form': form})

