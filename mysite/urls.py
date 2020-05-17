from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('getAllUsers/',views.userdetails,name="userDetails"),
    path('getUserActDetails/',views.index,name="completeDetails")

]