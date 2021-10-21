from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def index(request):
	return render(request, 'home.html', {})

def juan(request):
	return render(request, 'juan.html', {})

def info(request):
	return render(request, 'info.html', {})


