from django.urls import path, include

from .models import Post

from django.views.generic import ListView, DetailView
urlpatterns = [

    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date"),
    template_name="news_page/index.html"
    )),
    path('/<int:pk>/', DetailView.as_view(model=Post, template_name="news_page/post.html"))
]
