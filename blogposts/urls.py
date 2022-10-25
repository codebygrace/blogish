from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.new_post, name = 'new_post'),
    path('post/<int:id>/', views.post, name ='post'),
    path('post/<int:id>/edit', views.edit_post, name = 'edit_post'),
    path('post/<int:id>/update', views.update_post, name = 'update_post'),
    path('post/<int:id>/delete', views.delete_post, name='delete_post'),
    path('about/', views.about_page, name = 'about'),
    path('contact/', views.contact_page, name = 'contact'),
]