from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login, authenticate


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))
    account = forms.ModelChoiceField(queryset=Account.objects.filter(active=True).order_by('name'), 
                                     required=True, 
                                     widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        
    def clean_account(self):
        data = self.cleaned_data['account']
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError("Login ou senha invalidos.")

        for u in data.users.all():
            if u.id == user.id:
                return data

        raise forms.ValidationError("Esse Usuário não pertence a essa conta.")


  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'password1', 'password2', 'account']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}))
    account = forms.ModelMultipleChoiceField(queryset=Account.objects.filter(active=True).order_by('id'),
                                     initial=Account.objects.filter(active=True).first(),
                                       widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect select2 '}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biografia'}))

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'active', 'users']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da Conta'}))
    active = forms.BooleanField(initial=True, widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}))
    users = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect select2'})
    )
 
    def __init__(self, *args, **kwargs):
        account = kwargs.pop('account', None)  
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        self.fields['users'].widget.attrs['class'] = 'form-control'
        self.fields['users'].initial = CustomUser.objects.all().first()    

        if account:
            self.fields['name'].initial = account.name
            self.fields['active'].inital = account.active
            self.fields['users'].initial = account.users.all()
        
            
        
class PlantForm(forms.Form):
   

    name = forms.ModelChoiceField(queryset=Plant.objects.all().order_by('name'), 
                                     required=True, 
                                     widget=forms.Select(attrs={"class": "form-control"}))
    
    age = forms.IntegerField()
    latitude =  forms.DecimalField(max_digits=9, decimal_places=6)
    longiture = forms.DecimalField(max_digits=9, decimal_places=6)

    def __init__(self, *args, **kwargs):
        tree = kwargs.pop('tree', None)
        super(PlantForm, self).__init__(*args, **kwargs)

        self.fields['latitude'].widget.attrs['class'] = 'form-control '
        self.fields['longiture'].widget.attrs['class'] = 'form-control '
        self.fields['age'].widget.attrs['class'] = 'form-control'

        if tree:
            self.fields['name'].initial = tree.plant
            self.fields['latitude'].initial = tree.latitude
            self.fields['longiture'].initial = tree.longiture
            self.fields['age'].initial = tree.age


class ProfileForm(forms.Form):
    
    username = forms.CharField( required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Username'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}))
    bio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biografia'}))
    accounts = forms.ModelMultipleChoiceField(queryset=Account.objects.filter(active=True).order_by('id'),
                                     initial=Account.objects.filter(active=True).first(),
                                       widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect select2 '}))
    
    

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            profile = user.get_profile()
            self.fields['accounts'].initial = user.accounts.all()
            if profile:
                self.fields['bio'].initial = profile.bio

    

