from django.shortcuts import render
from uploadAbstract.forms import UserForm
from mainApp.models import SiteSetting


def index(request):

    site_settings = SiteSetting.objects.all().first()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'uploadAbstract/successPage.html', {'site_settings': site_settings})

        else:
            print form.errors
    else:
        form = UserForm()

    return render(request, 'uploadAbstract/uploadAbstract.html', {'form': form, 'site_settings': site_settings})
