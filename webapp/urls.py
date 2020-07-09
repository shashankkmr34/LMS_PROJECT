"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('load_form_sales', views.load_form_sales),
    path('addsales', views.addsales),
    path('load_form_leads', views.load_form_leads),
    path('addleads', views.addleads),
    path('show', views.show),
    path('show_leads', views.show_leads),
    path('edit/<int:id>', views.edit),
    path('edit_leads/<int:id>', views.edit_leads),
    path('update/<int:id>', views.update),
    path('update_leads/<int:id>', views.update_leads),
    path('delete/<int:id>', views.delete),
    path('delete_leads/<int:id>', views.delete_leads)


]
