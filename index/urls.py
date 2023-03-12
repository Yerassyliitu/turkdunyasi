from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.defaulttags import url
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import MyView, login_view, logout_view
# app_name = 'index'
urlpatterns = [
    path('', views.index, name="index"),
    path('university/', views.catalog, name="catalog"),
    path('university/<int:university_id>/', views.university, name="university"),
    path('client_form/', views.client_form, name="client_form"),
    path('', MyView.as_view(), name='myview'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


