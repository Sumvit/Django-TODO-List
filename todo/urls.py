from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView
urlpatterns = [
  path('',RedirectView.as_view(url='/tasks/')),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.signin_view, name='login'),
    path('logout/',  views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('delete/<int:task_id>/', views.remove_task, name='delete_task'),
    path('update/<int:task_id>/',views.update_task,name='update_task')
]
