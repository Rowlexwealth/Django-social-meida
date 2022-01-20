from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:id>', views.rooms, name = 'rooms'),
    path('profile/<int:id>', views.userProfile, name = 'user-profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:id>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:id>/', views.deleteRoom, name='delete-room'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('delete-message/<int:id>/', views.deleteMessage, name='delete-message'),

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]
