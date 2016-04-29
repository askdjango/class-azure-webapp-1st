from django.shortcuts import redirect, render
from django.contrib.auth.views import login
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

