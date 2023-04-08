from django import forms
from .models import Client_forms
from django.contrib.auth.forms import AuthenticationForm


class MyFilterForm(forms.Form):
    country = forms.ChoiceField(choices=[('Все', 'Все'), ('Китай', 'Китай'), ('Турция', 'Турция')], required=False, widget=forms.Select(attrs={'class': 'form-control'}), initial='Все')
    price = forms.ChoiceField(choices=[('Все', 'Все'), (500, 500), (1500, 1500), (2200, 2200), (2800, 2800)], required=False, widget=forms.Select(attrs={'class': 'form-control'}), initial='Все')
    program = forms.ChoiceField(choices=[('Все', 'Все'), ('Квота для иностранца', 'Квота для иностранца'), ('Платная', 'Платная'), ('Правительственный грант', 'Правительственный грант')], required=False, widget=forms.Select(attrs={'class': 'form-control'}), initial='Все')



class ClientForm(forms.ModelForm):
    name = forms.CharField(
        label='Ваше Имя:',
        required=True,  # Keep the field required
        error_messages={'required': 'Пожалуйста, введите ваше имя.'},  # Customize the error message
        widget=forms.TextInput(attrs={'class': 'form-select', 'style': 'width: 300px'})
    )

    COUNTRY_CHOICES = [
        ('Образование в Турции', 'Образование в Турции'),
        ('Образование в Китае', 'Образование в Китае'),
        ('Образование в Турции и Китае', 'Образование в Турции и Китае')
    ]
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        label='Какая страна вас интересует?',
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px'}),
    )

    LANGUAGE_CHOICES = [
        ('Русский', 'Русский'),
        ('Казахский', 'Казахский')
    ]

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label='Выберите язык консультации:',
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px'}),
    )

    SCHOOL_CLASSES_CHOICES = [
        ('Заканчиваю 11 класс', 'Заканчиваю 11 класс'),
        ('Заканчиваю Колледж', 'Заканчиваю Колледж'),
        ('Я родитель 11 классника', 'Я родитель 11 классника')
    ]

    school_class = forms.ChoiceField(
        choices=SCHOOL_CLASSES_CHOICES,
        label='В каком вы классе?',
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px'}),
    )

    number = forms.CharField(
        label='Телефон',
        error_messages={'invalid': 'Неверный формат номера телефона'},
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона в формате +7xxxxxxxxxx', 'style': 'width: 300px'})
    )

    class Meta:
        model = Client_forms
        fields = "__all__"




class OwnerLoginForm(AuthenticationForm):
    pass