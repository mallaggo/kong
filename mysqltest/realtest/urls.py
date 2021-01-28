from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('structure/', views.structure, name='structure'),
    path('', views.index, name='index'),
    path('showindex/', views.showindex, name='showindex'),
    path('showdetail/<int:pk>', views.showdetail, name='showdetail'),
    path('product/<int:pk>', views.product, name='product'),
    path('productshow', views.productshow, name='productshow'),
    path('blog/', views.blog_index, name='blog_index'),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/<category>/", views.blog_category, name="blog_category"),
    path("product_write/", views.product_write, name="product_write"),

]

