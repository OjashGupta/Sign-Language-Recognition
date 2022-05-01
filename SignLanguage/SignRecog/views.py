from django.shortcuts import render
from .import signrecognition

def home(request):
    return render(request, "index.html")


def read_sign(request):
    signrecognition.recognize_sign()
    return render(request, "index.html")