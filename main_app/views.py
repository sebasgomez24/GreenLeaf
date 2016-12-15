from django.contrib.auth import authenticate,get_user_model, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django import forms
from .forms import LoginForm, RegisterForm, StrainForm, BannerForm
from .models import Strain

# Create your views here.

def index(request):
	login_form = LoginForm()
	register_form = RegisterForm()
	return render(request, 'index.html', {'login_form':login_form, 'register_form':register_form})

def profile(request, username):
	strains = Strain.objects.all().order_by('-timestamp')
	strain_form = StrainForm()
	banner_form = BannerForm()
	return render(request, 'profile.html', {'strains':strains, 'strain_form':strain_form, 'banner_form':banner_form})

def register(request):
	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			user = register_form.save(commit=False)
			password = register_form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			new_user = authenticate(username=user.username, password=password)
			if new_user is not None and new_user.is_active:
				login(request, new_user)
				messages.success(request, "You've created a new profile")
				return redirect('profile', new_user)
			else:
				messages.error(request, 'Something went wrong with your registration')
			return redirect('register/')
	else:
		register_form = RegisterForm()
	return render(request, 'index.html', {'register_form':register_form})

def login_view(request):
	register_form = RegisterForm()
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect('profile', user)
			else:
				messages.error(request, 'Incorrect username/password combination')
				return redirect('/')
	else:
		login_form = LoginForm()
	return render(request, 'index.html', {'login_form':login_form, 'register_form':register_form})

def logout_view(request, user):
	logout(request)
	return HttpResponseRedirect('/')

def strains(request, username):
	strains = Strain.objects.all().order_by('-timestamp')
	strain_list = Strain.objects.all().order_by('-timestamp')
	paginator = Paginator(strain_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		strains = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		strains = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		strains = paginator.page(paginator.num_pages)
	query = request.GET.get('query')
	if query:
		strains = strain_list.filter(
			Q(name__icontains=query) | Q(description__icontains=query) | Q(strain_type__icontains=query)
		).order_by('-timestamp').distinct()
	return render(request, 'strains.html', {'strains':strains})

def upload_strain(request, username):
	strain_form = StrainForm(request.POST, request.FILES or None)
	if strain_form.is_valid():
		strain = strain_form.save(commit=False)
		strain.user = request.user
		strain.save()
		messages.success(request, 'You have created a new post' )            
		return redirect('profile', username)
	else:
		messages.error(request, 'Not Successfully Created')
	context = {
		'strain_form': strain_form
	}
	return render(request, 'profile.html', context)

def banner_color(request, username):
	strain_form = StrainForm()
	banner_form = BannerForm()
	if request.method=='POST':
		banner_form = BannerForm(request.POST)
		if banner_form.is_valid():
			color = banner_form.cleaned_data
			color_ = color.get('color')
			return redirect('profile', username)
	else:
		messages.error(request, 'Color Not Changed')
	context = {
		'color': color,
		'banner_form': banner_form,
		'strain_form': strain_form,
	}
	return render(request, 'profile.html', context)

def detail(request, slug):  
    strain = get_object_or_404(Strain, slug=slug)
    sleepyness_val = strain.sleepy
    creativity_val = strain.creative
    munchies_val = strain.hungry
    giggles_val = strain.giggles
    happy_val = strain.happy
    relaxed_val = strain.relaxed
    pain_val = strain.pain
    stress_val = strain.stress
    insomnia_val = strain.insomnia
    depression_val = strain.depression
    lack_of_appetite_val = strain.lack_of_appetite
    paranoia_val = strain.paranoia
    cotton_mouth_val = strain.cotton_mouth
    dry_eyes_val = strain.dry_eyes
    headache_val = strain.headache
    eighth = strain.eighth_price
    quarter = strain.quarter_price
    half = strain.half_price
    ounce = strain.ounce_price
    context = {
    	'strain': strain,
    	'sleepyness': sleepyness_val,
    	'creativity': creativity_val,
    	'munchies': munchies_val,
    	'giggles': giggles_val,
    	'happy': happy_val,
    	'pain': pain_val,
    	'insomnia': insomnia_val,
    	'depression': depression_val,
    	'lack_of_appetite': lack_of_appetite_val,
    	'paranoia': paranoia_val,
    	'cotton_mouth': cotton_mouth_val,
    	'dry_eyes': dry_eyes_val,
    	'headache': headache_val,
    	'eighth': eighth,
    	'quarter': quarter,
    	'half': half,
    	'ounce': ounce,
    }
    return render(request, 'detail.html', context)

def update_page(request, username):
	strains = Strain.objects.all().order_by('-timestamp')
	context = {
		'strains': strains,
	}
	return render(request, 'update-page.html', context)

def update_strain(request, slug):
	strain = get_object_or_404(Strain, slug=slug)
	instance = get_object_or_404(Strain, slug=slug)
	form = StrainForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, 'You have updated your Strain!')            
		return redirect('profile', instance.user)
	context = {
		'strain': strain,
		'form': form,
	}
	return render(request, 'update-strain.html', context)

def delete_strain(request, slug=None): 
    strain = get_object_or_404(Strain, slug=slug)
    if request.user == project.user:
        messages.success(request, 'You have deleted your post')
        strain.delete()
    return redirect('profile', strain.user)
