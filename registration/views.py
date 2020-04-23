from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
# Create your views here.

def home_view(request):
	return render(request,'home.html')
	
def signup_view(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save();
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect(home_view)
	return render(request, 'signup.html', {'form': form})

def login_view(request):
	form = AuthenticationForm(data = request.POST)
	if request.method == 'POST':
		if form.is_valid():
			return render(request,'/getprediction')
	else:
		form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form':form})
