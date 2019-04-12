from django.urls import path
from accounts import views
urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),
    path('dashbord/',views.dashbord,name="dashbord")
]