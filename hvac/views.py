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
from azure.storage.blob import BlobServiceClient, generate_container_sas, ContainerSasPermissions, ContainerClient

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
    values['Header_temp'] = json.loads(result['Header_temp'])
    values['HX_temp'] = json.loads(result['HX_temp'])
    values['time'] = result['time']
    values['capa_s'] = int(result['capa_s'])
    values['capa_r'] = int(result['capa_r'])
    values['cool_s'] = int(result['cool_s'])
    values['cool_r'] = int(result['cool_r'])
    return render(request, "tables/table1.html", context = values)

def page_hvac(request):
    # 모델스토리지 연결
    blob_storage_account = 'hvacstorage'
    blob_storage_container = 'borame-loadpred'
    blob_storage_key = 'jnJ3rPaeF08fafa0iP9NDbit7Flu92P57iOcm3IRsMDmdl88rYzIY7i7igZ+727gyvw+RYa9QT6ZFEeEZCSQ3w=='

    permission = ContainerSasPermissions(read=True, write=True, 
                                            delete=True, list=True, 
                                            delete_previous_version=True, 
                                            tag=True)
    sas_token = generate_container_sas(account_name=blob_storage_account,
                                        container_name=blob_storage_container,
                                        account_key=blob_storage_key,
                                        permission=permission,
                                        expiry='2025-02-24T15:33:13Z')

    url = "https://"+blob_storage_account+".blob.core.windows.net/"+blob_storage_container
    container_client = ContainerClient.from_container_url(container_url=url, credential=sas_token)

    # 스토리지 파일 저장 result.json 이름으로...
    blob_client = container_client.get_blob_client("result.json")
    streamdownloader = blob_client.download_blob()
    result = json.loads(streamdownloader.readall())
    values = json.loads(result['result'])
    values['index_col'] = result['index_col']
    values['pred'] = [round(i/3024, -1) for i in result['pred']]
    values['meas'] = [round(i/3024, -1) for i in result['meas']]
    values['max_pred'] = max(values['pred'])
    values['time'] = result['time']
    a = [1 if i == 'ON' else 0 for i in list(json.loads(result['opt_out'])['냉동기'].values())]
    b = [500, 500, 500, 250, 250, 250, 250]
    c = [a[i]*b[i] for i in range(0, 7)]
    values['Capa'] = sum(c)
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
    values['df6_index'] = list(values['df6']['청구년월'].values())
    values['df6_val1'] = list(values['df6']['기본요금'].values())
    values['df6_val2'] = list(values['df6']['전력사용요금'].values())
    return render(request, "tables/page_elec.html", context = values)

def page_peak(request):
    return render(request, "tables/page_peak.html")

def page_occupancy(request):
    return render(request, "tables/page_occupancy.html")
