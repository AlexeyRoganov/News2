from django.views.generic import ListView
# импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import PostFilter

class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'post.html'
# указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'post'
# это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')

    ordering = ['title']
    paginate_by = 1


class PostsList2(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'
# указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
# это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')

    ordering = ['title']
    paginate_by = 1

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context