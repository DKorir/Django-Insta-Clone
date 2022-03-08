from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from . models import Category, Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list': cat_menu_list})

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category= cats.replace('-',' '))
    return render(request,'categories.html',{'cats': cats.replace('-',' ').title(),'category_posts': category_posts})
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddPostView,self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context