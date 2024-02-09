from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link


def scrape(request):
    if request.method == 'POST':
        site = request.POST['site']

        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')

        for link in soup("a"):
            # Displaying on our webpage
            link_address = link.get("href")
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, "myapp/result.html", {"data": data})


# Delete method
def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
