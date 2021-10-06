from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name='index'),
    path("login/",views.Login,name='login'),
    path("signup/",views.signup,name='signup'),
    path("edit/<int:id>/",views.edit,name='edittodo'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('logout/',views.Logout,name="logout")
]
