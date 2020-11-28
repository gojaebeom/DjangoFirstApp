from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    # hello world list
    hello_world_list = HelloWorld.objects.all()

    if request.method == "POST":
        temp = request.POST.get('data1')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        return render(request, 'hello.html', context={'hello_world_list': hello_world_list})
