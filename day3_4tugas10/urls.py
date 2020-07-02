"""day3_4tugas10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from produk.views import index, tambah_produk, update_produk, delete_produk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('tambah_produk', tambah_produk, name='tambah_produk'),
    path('update_produk/<produk_id>', update_produk, name='update_produk'),
    path('delete_produk/<produk_id>', delete_produk, name='delete_produk'),
]
