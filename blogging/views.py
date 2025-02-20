# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class LatestPostsFeed(Feed):
    title = "Recent blogging posts"
    link = "/posts/"
    description = "Latest posts published on the blog"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])


# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
