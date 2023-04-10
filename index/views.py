import re

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.db.models import Q
from wtforms import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import *
from .form import MyFilterForm, ClientForm, OwnerLoginForm
from django.forms import ValidationError


class MyView(TemplateView):
    template_name = 'myapp/for_moderator.html'

    @login_required(login_url='index:login')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                client = Client_forms.objects.all()
                login(request, user)
                return render(request, 'index/for_moderator.html', {'client': client})
    else:
        form = AuthenticationForm()
    return render(request, 'index/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index:login'))



def index(request):
    universities = University.objects.all()
    china_universities = universities.filter(country='Китай')
    turkey_universities = universities.filter(country='Турция')
    images = Image_src.objects.all()
    context = {'universities': universities, 'images': images, 'china_universities': china_universities, 'turkey_universities': turkey_universities}
    return render(request, 'index/index.html', context)


def catalog(request):
    form = MyFilterForm(request.GET)
    query = request.GET.get('query')
    universities = University.objects.all()
    images = Image_src.objects.all()
    if query:
        universities = universities.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query) | Q(city__icontains=query))
    if form.is_valid():
        country = form.cleaned_data['country']
        price = form.cleaned_data['price']
        program = form.cleaned_data['program']
        if country != 'Все' and country:
            universities = universities.filter(country=country)
        if program != 'Все' and program:
            universities = universities.filter(program=program)
        if price != 'Все' and price:
            universities = universities.filter(price=price)
    context = {'universities': universities, 'images': images, 'query': query, 'form': form}
    return render(request, 'index/catalog.html', context)


def university(request, university_id):
    images = Image_src.objects.all()
    current_university = University.objects.get(pk=university_id)
    if current_university is not None:
        return render(request, 'index/university.html', {'current_university': current_university, 'images': images})
    else:
        raise Http404('Университет не найден.')


def search(request):
    query = request.GET.get('q')
    if query:
        results = University.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query) | Q(city__icontains=query) | Q(faculty__icontains=query))
    else:
        results = University.objects.none()
    context = {'results': results, 'query': query}
    return render(request, 'catalog.html', context)


def redirect_form(request):
    return render(request, 'index/redirect-form.html')


def client_form(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша форма была успешно отправлена.')
            return redirect('redirect-form')
        else:
            messages.error(request, 'Пожалуйста, заполните номер телефона корректно')
    else:
        form = ClientForm(request.GET)
    context = {'form': form}
    return render(request, 'index/client_form.html', context)


def delete_form(request, form_id):
    form = Client_forms.objects.get(pk=form_id)
    if request.method == "POST":
        form.delete()
        client = Client_forms.objects.all()
        return render(request, 'index/for_moderator.html', {'client': client})
    print('alo2')
    return render(request, 'index/for_moderator.html')


