from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from .models import Strain

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    authentication_code = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            'authentication_code',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has already been registered')
        return email

class StrainForm(forms.ModelForm):
    eighth_price = forms.IntegerField(
        label = 'price for 1/8oz',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount in Whole Numbers (20, 40 ...)'})
    )
    quarter_price = forms.IntegerField(
        label = 'price for 1/4oz',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount in Whole Numbers (20, 40 ...)'})
    )
    half_price = forms.IntegerField(
        label = 'price for 1/2oz',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount in Whole Numbers (20, 40 ...)'})
    )
    ounce_price = forms.IntegerField(
        label = 'price for 1oz',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount in Whole Numbers (20, 40 ...)'})
    )
    sleepyness = forms.IntegerField(
        label = 'How sleepy does it make you?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    creativity = forms.IntegerField(
        label = 'How creative does it make you?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    munchies = forms.IntegerField(
        label = 'Does it give you the munchies?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    giggles = forms.IntegerField(
        label = 'Does it make you laugh?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    chill = forms.IntegerField(
        label = 'How relaxed do it make you?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    happy = forms.IntegerField(
        label = 'How happy does it make you?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    pain = forms.IntegerField(
        label = 'How much does it help with Pain?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    stress = forms.IntegerField(
        label = 'How much does it help with Stress?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    insomnia = forms.IntegerField(
        label = 'How much does it help with Insomnia?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    depression = forms.IntegerField(
        label = 'How much does it help with Depression?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    lack_of_appetite = forms.IntegerField(
        label = 'How much does it help with appetite?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    paranoia = forms.IntegerField(
        label = 'Does it make you paranoid?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    cotton_mouth = forms.IntegerField(
        label = 'Does it give you cotton mouth?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    dry_eyes = forms.IntegerField(
        label = 'Does it give you dry eyes?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    headache = forms.IntegerField(
        label = 'Does it give you a headache?',
        help_text='<div class="helptext">Drag to the right to increase (max is 10, default is 0)</div>',
        widget=forms.NumberInput(attrs={'type':'range','min':'1', 'max':'10', 'step':'1', 'value':'0'})
    )
    class Meta:
        model = Strain
        fields = [
            'name', 'initials', 'strain_type', 'eighth_price', 'quarter_price', 'half_price', 'ounce_price', 
            'sleepyness' ,'creativity', 'munchies', 'giggles', 'chill', 'happy', 'pain', 'stress', 
            'insomnia', 'depression', 'lack_of_appetite', 'paranoia', 'cotton_mouth', 'dry_eyes', 'headache', 
            'description', 'image'
        ]

class BannerForm(forms.Form):
    banner_color_choices = (
        ('#8AA236', 'green'),
        ('#236467', 'blue'),
        ('#592A71', 'purple'),
    )
    banner_color = forms.MultipleChoiceField(
        widget=forms.Select,
        choices=banner_color_choices,
    )

class AmountForm(forms.Form):
    amount_choices = (
        ('1/8oz', '1/8oz'),
        ('1/4oz', '1/4oz'),
        ('1/2oz', '1/2oz'),
        ('1oz', '1oz'),
    )
    amount = forms.MultipleChoiceField(
        widget=forms.Select,
        choices=amount_choices,
    )