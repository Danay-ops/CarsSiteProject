from django.urls import path, re_path
from . import views
from .views import page_not_found
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('', views.index, name='home'), # Подключаем автоматом все маршруты # http://127.0.0.1:8000/
    path('', views.CarsHome.as_view(), name='home'),
    path('about/', views.about, name ='about'),
   # path('addpage/',views.addpage, name = 'add_page'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('categories/<slug:cat_slug>/', views.show_categories, name='category'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),

]

