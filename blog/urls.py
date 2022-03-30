from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('user/<int:pk>', views.profile, name='profile'),
    path('add-post', views.add_post, name='add-post')
]