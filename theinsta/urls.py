from django.urls import path
from .views import AddCategoryView, AddPostView, ArticleDetailView, CategoryListView, DeletePostView, HomeView, DetailView, UpdatePostView,CategoryView, LikeView
# from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail" ),
    path('add_post/',AddPostView.as_view(), name="add_post"),
    path('add_category/',AddCategoryView.as_view(), name="add_category"),
     path('article/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
]
