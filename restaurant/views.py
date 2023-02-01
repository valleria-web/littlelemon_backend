from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<div style='background-color: yellow; text-align: center;'><h1 style='color: green; font-size: 100px; font-family: Arial'>Little Lemon is cooking <h2 style='color: orange; text-align: center; font-size: 90px;'>The dishes will be ready soon <h3 style='color: text-align: center; black; font-size: 50px; font-family: Arial'>Thank you for your patience :) </h2></div>")