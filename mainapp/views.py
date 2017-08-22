from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response


def main(request):
    return render_to_response("index.html")
