from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import json
import pkg_resources
import subprocess
import sys
import os
import ssl
from datetime import datetime, timedelta

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
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param':{'date':(datetime.now() + timedelta(hours=9)).strftime('%Y-%m-%d')}}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-borame-opthvac/score'
    api_key = 'BUZ6X7bFowLNqM7AhFeC71C9EzyxOeXd' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    values = json.loads(result['result'])
    values['index_col'] = result['index_col']
    values['pred'] = result['pred']
    values['meas'] = result['meas']
    values['max_pred'] = max(values['pred'])
    values['time'] = result['time']
    values['opt_out'] = json.loads(result['opt_out'])
    return render(request, "tables/page_hvac.html", context = values)

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
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-borame-elec/score'
    api_key = 'NogOkGsn8WcVNLfhuDFc6vYNPumr0K0w' # Replace this with the API key for the web service
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
    values['df5'] = json.loads(result['df5'])
    values['df6'] = json.loads(result['df6'])
    values['df2_index'] = list(values['df2']['시간'].values())
    values['df2_elec'] = list(values['df2']['전력량'].values())
    values['df2_peak'] = list(values['df2']['peak'].values())
    return render(request, "tables/page_elec.html", context = values)

def page_peak(request):
    return render(request, "tables/page_peak.html")

def page_occupancy(request):
    return render(request, "tables/page_occupancy.html")
