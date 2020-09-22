from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['name'] = "Jahid Hasan"
    context['country'] = "Bangladesh"

    return context

def index(request):
    return render(request, "hello/index.html")

def jahid(request):
    return HttpResponse("Hello, Jahid!")

def farhana(request):
    return HttpResponse("Hello, Farhana Khanom Ruma")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()
        })
