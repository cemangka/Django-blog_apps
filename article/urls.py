from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView,ArticleListCategoryView
urlpatterns = [
        url(r'^category/(?P<category>[\w]+)/(?P<page>\d+)$',ArticleListCategoryView.as_view(), name = 'category'),
        url(r'^(?P<page>\d+)$',ArticleListView.as_view(), name = 'list'),
        url(r'detail/(?P<slug>[\w-]+)$', ArticleDetailView.as_view(), name = 'detail'),
    ]