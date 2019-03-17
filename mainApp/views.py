from django.shortcuts import render
from .forms import SubscriberForm


def index(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'mainApp/homePage.html', locals())
