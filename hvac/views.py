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


# def hello(request):
#     return HttpResponse("Hello, World!")

def index(request):

    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param':{'bld':1}}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-ocb-control/score'
    api_key = 'kwea4NGIHAlBO1g5P6M4fQ5dVSb2D5Lz' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

    values = json.loads(result['table'])
    values['Tcount'] = result['count']
    values['time'] = result['time']
    values['pm10'] = result['pm10']
    values['index_pm10'] = result['index_pm10']
    values['pm25'] = result['pm25']
    values['index_pm25'] = result['index_pm25']
    return render(request, "tables/table1.html", context = values)
