from django.urls import path
from . import views
from .views import MyView, login_view, logout_view
urlpatterns = [
    path('', views.index, name="index"),
    path('university/', views.catalog, name="catalog"),
    path('university/<int:university_id>/', views.university, name="university"),
    path('client_form/', views.client_form, name="client_form"),
    path('myview/', MyView.as_view(), name='myview'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete-form/<int:form_id>/', views.delete_form, name="delete-form"),
    path('redirect-form', views.redirect_form, name="redirect-form")
]


