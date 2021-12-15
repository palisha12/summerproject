"""AppointmentSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import home, loginPage, RegisterPage,LogoutPage
from member.views import submitted,adminhome,status1,status2,search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('submitted',submitted,name='submitted'),
    path('adminhome',adminhome,name='adminhome'),
    path('status1/<str:pk>',status1, name='status1'),
    path('status2/<str:pk>',status2, name='status2'),
    path('search',search,name='search'),
    path('login/', loginPage,name='loginPage'),
    path('register/', RegisterPage,name='RegisterPage'),
    path('logout/', LogoutPage,name='LogoutPage'),


]
