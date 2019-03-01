from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/edit/<int:id>/', views.edit, name='edit'),
    path('create/delete/<int:id>/', views.delete, name='delete'),
    # path('teacher/delete/<int:id>/', views.teacher, name='teacher'),
]
