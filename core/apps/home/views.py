from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("this is demo page")


def main(request):
    return render(request, 'index.html')