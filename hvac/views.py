from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import json
import pkg_resources
import subprocess
import sys
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def index(request):
    return render(request, "tables/table1.html")

def page_hvac(request):
    return render(request, "tables/page_hvac.html")

def page_temp(request):
    return render(request, "tables/page_temp.html")

def page_cool(request):
    return render(request, "tables/page_cool.html")

def page_elec(request):
    return render(request, "tables/page_elec.html")

def page_peak(request):
    return render(request, "tables/page_peak.html")
