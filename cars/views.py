from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from cars.forms import AddPostForm, UploadFileF, ContactForm
from cars.models import Cars, Categories, UploadF

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'}
     #   {'title': "Войти", 'url_name': 'login'}
]




"""def index(request): # с помощью request мне доступна вся инфа о текущем запросе
    posts= Cars.published.all()
    data ={
        'menu' : menu,
        'title' : 'Главная страница',
        'posts' : posts
    }
    return render(request,'cars/index.html', data)""" # Не забывай передавать данные в шаблон

"""def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)"""

class CarsHome(ListView):
   # model = Cars
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    extra_context = {
        'menu': menu,
        'title': 'Главная страница',
    }

    def get_queryset(self):
        return Cars.published.all()




"""def about(request):
    if request.method == "POST":
        form = UploadFileF(request.POST,request.FILES)
        if form.is_valid():
         fp=UploadF(file=form.cleaned_data['file'])
         fp.save()
    else:
        form = UploadFileF()
    data = {
        'menu': menu,
        'title': "О сайте",
        'form': form
    }
    return render(request,'cars/about.html',data)"""


def about(request):
    data = {
        'menu': menu,
        'title': "О сайте",
    }
    return render(request,'cars/about.html',data)




def show_post(request, post_slug):
    post = get_object_or_404(Cars,slug=post_slug) # Когда я хочу получить обьект класса обращаюсь к этому методу get
    data = {
        'title': post.title,
        'content':post.content,
        'menu': menu,
        'post': post,
        'cat_selected':1
    }
    return render(request, 'cars/post.html', data)

class ShowPost(DetailView):
    model = Cars
    template_name = 'cars/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

def show_categories(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Cars.published.filter(cat_id=category)
    paginate_by= 1
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request,'cars/index.html', context=data )

"""class CarsCategory(ListView):
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return  Cars.published.filter(cat_slug=self['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title']= 'Категория -' +cat.name
        context['menu']= menu
        context['cat_selected']= cat.pk
        return context
"""

"""def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
          #  print(form.cleaned_data)
         """"""try:
                Cars.objects.create(**form.cleaned_data)
                return redirect('home')
         except:
                form.add_error(None,'Ошибка заполнения формы')""""""
        form.save()
        return redirect('home')
    else:
        form = AddPostForm()
    data = {
        'menu': menu,
        'title': "Добавить",
        'form': form
    }
    return render(request,'cars/addpage.html',data)"""

class AddPage(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
   # model = Cars
   # fields = ['title', 'slug', 'content','photo','is_published', 'cat']
    template_name = 'cars/addpage.html'
   # success_url = reverse_lazy('home')
    login_url = 'users:login'
    extra_context = {
        'menu': menu,
        'title': "Добавить",
    }

    def form_valid(self, form):
        w = form.save(commit = False)
        w.author = self.request.user
        return super().form_valid(form)

class UpdatePage(UpdateView):
     model = Cars
     fields = ['title', 'content','photo','is_published', 'cat']
     template_name = 'cars/addpage.html'
     success_url = reverse_lazy('home')
     extra_context = {
        'menu': menu,
        'title': "Редактировать",
     }

class DeletePage(DeleteView):
    model = Cars
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'cars/deletepage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': "Удалить",
    }


"""class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'menu': menu,
            'title': "Добавить",
            'form': form
        }
        return render(request, 'cars/addpage.html', data)
    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'menu': menu,
            'title': "Добавить",
            'form': form
        }
        return render(request, 'cars/addpage.html', data)"""

"""class AddPage(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
   # model = Cars
   # fields = ['title', 'slug', 'content','photo','is_published', 'cat']
    template_name = 'cars/addpage.html'
   # success_url = reverse_lazy('home')
    login_url = 'users:login'
    extra_context = {
        'menu': menu,
        'title': "Добавить",
    }

    def form_valid(self, form):
        w = form.save(commit = False)
        w.author = self.request.user
        return super().form_valid(form)"""




@login_required
def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ContactForm()
    form = ContactForm()
    data = {
        'menu': menu,
        'title': "Обратная связь",
        'form': form,

    }
    return render(request, 'cars/contact.html', data)


def login(request):
    return HttpResponse('Логин')
def page_not_found(request,exception):
    return HttpResponse('<h1>Упсс...</h1>')


