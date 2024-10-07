from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import cash_entry_form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm
# Create your views here
def app_view(request):
    if request.method == 'POST':
        form = cash_entry_form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('cash_entry')  
    else:
        form = cash_entry_form()  
    
    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cash_entry')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
