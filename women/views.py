from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, include
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from .forms import *
from .models import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin

#menu = [{'title': "О сайте", 'url_name': 'about'},
#        {'title': "Добавить статью", 'url_name': 'add_page'},
#        {'title': "Обратная связь", 'url_name': 'contact'},
#        {'title': "Войти", 'url_name': 'login'}
#]


#def index(request):
#    posts = Women.objects.all()
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Главная страница',
#        'cat_selected':0,
#    }
#    return render(request, 'women/index.html', context=context)
class WomenHome(DataMixin,ListView):

    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')

class AboutView(DataMixin, TemplateView):
    template_name = 'women/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О сайте")
        # old way return dict(list(context.items()) + list(c_def.items()))
        context.update(c_def)
        return context


class AddPage(LoginRequiredMixin,DataMixin,CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

def adminka(request):
    return render(request,'admin',{'menu':menu,'title':'adminka'})

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        context.update(c_def)
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class WomenCategory(DataMixin,ListView):

    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)

       #old return dict(list(context.items()) + list(c_def.items()))
        return {**context, **c_def}

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True).select_related('cat')

class ShowPost(DataMixin,DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return {**context, **c_def}
#def show_post(request, post_slug):
#    post = get_object_or_404(Women, slug=post_slug)
#    context = {
#        'post':post,
#        'menu':menu,
#        'title':post.title,
#        'cat_selected':1,
#    }
#    return render(request,'women/post.html',context=context)

#def show_category(request, cat_slug):
#    posts = Women.objects.filter(cat__slug=cat_slug)
#
#    context={
#        'title':'Отображение по рубрикам',
#        'posts':posts,
#        'cat_selected':cat_slug,
#        'menu':menu,
#    }
#    return render(request,'women/index.html',context=context)

#class RegisterUser(DataMixin,CreateView):
#    form_class = RegisterUserForm
#    template_name = 'women/register.html'
#    success_url = reverse_lazy('login')
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Регистрация")
#        return dict(list(context.items()) + list(c_def.items()))
#
#    def form_valid(self, form):
#        user = form.save()
#        login(self.request, user)
#        return redirect('home')
#
#class LoginUser(DataMixin, LoginView):
#    form_class = LoginUserForm
#    template_name = 'women/login.html'
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Авторизация")
#        return dict(list(context.items()) + list(c_def.items()))
#
#    def get_success_url(self):
#        return reverse_lazy('home')
#
def logout_user(request):
    logout(request)
    return redirect('/')

#class LoginAllauth(DataMixin,LoginView):
#    template_name = include('allauth.urls')
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Авторизация")
#        return dict(list(context.items()) + list(c_def.items()))
#
#    def get_success_url(self):
#        return reverse_lazy('home')