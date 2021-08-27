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
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-borame-main/score'
    api_key = 'bNxBFk8mDGy4OWxYsu5vlAulYglVUCh1' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    values = json.loads(result['df1'])
    values['df1'] = json.loads(result['df1'])
    values['df2'] = json.loads(result['df2'])
    values['df3'] = json.loads(result['df3'])
    values['time'] = result['time']
    values['capa_s'] = int(result['capa_s'])
    values['capa_r'] = int(result['capa_r'])
    return render(request, "tables/table1.html", context = values)

def page_hvac(request):
    return render(request, "tables/page_hvac.html")

def page_temp(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-borame-tempload/score'
    api_key = 'sWdF9CmWaZmVgxN1OgzrFDCHvgE20ZNX' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    values = json.loads(result['df1'])
    values['df1'] = json.loads(result['df1'])
    values['df2'] = json.loads(result['df2'])
    return render(request, "tables/page_temp.html", context = values)

def page_cool(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-borame-tempload/score'
    api_key = 'sWdF9CmWaZmVgxN1OgzrFDCHvgE20ZNX' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    values = json.loads(result['df1'])
    values['df1'] = json.loads(result['df1'])
    values['df2'] = json.loads(result['df2'])
    values['text'] = json.loads(result['text'])
    return render(request, "tables/page_cool.html", context = values)

def page_elec(request):
    return render(request, "tables/page_elec.html")

def page_peak(request):
    return render(request, "tables/page_peak.html")
