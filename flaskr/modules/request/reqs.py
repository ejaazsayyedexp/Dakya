from flask import (Blueprint, redirect, render_template, url_for, request)
import json

import requests
from datetime import datetime

from ..formDataProcessor.processFormData import processForm

bp = Blueprint('reqs',__name__,url_prefix='/reqs')

@bp.route('/',methods=['GET'])
def trial():
    return json.dumps({'status':'Successfully working'})

@bp.route('/makeRequest',methods=('GET','POST'))
def makeRequest():
    print('Request is made on:'+str(datetime.now()))
    if(request.method=='POST'):
        formData = dict(request.form)
        link, form_data, header, request_type = processForm(formData)
        #print(link,form_data,header, request_type)
        #Might need to call for the history recording here

        #Set headers to json
        # header = {'Content-type':'application/json',
        # 'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzEwOTIxNDQsImp3dElkIjoiZjkydjIiLCJ1c2VyIjp7InVzZXJfaWQiOjEsInVzZXJuYW1lIjoidGVzdCIsImZpcnN0X25hbWUiOiJUZXN0IiwibGFzdF9uYW1lIjoiVXNlciIsImxhc3RfbG9naW4iOiIyMDIyLTEyLTE1VDA4OjE1OjU0LjQ1MVoiLCJjcmVhdGVkX2RhdGUiOiIyMDIyLTEyLTE1VDA1OjQ4OjAzLjA5MFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDIyLTEyLTE1VDA1OjQ4OjAzLjA5MFoifSwiZXhwIjoxNjcxMTM1MzQ0fQ.Cza9FZnrIjMuBFLR8XTWp3fPXxSzwu9IB4Y0ITfE6Ng',
        #     'x-api-key':'A26B25C24D23E22F21G20H19I18J17K16L15M14N13O12P11Q10R9S8T7U6V5W4X3Y2Z1'
        # }
        #Check for the request type

        if(request_type=='GET'):
            # resp = requests.get(link,headers=header)
            # print(resp.json())
            # return render_template('requestFor.html', response_data=resp.json())
            try:
                resp = requests.get(link,headers=header)
                return render_template('requestFor.html', response_data=resp.json())
            except(requests.exceptions.JSONDecodeError):
                return render_template('requestFor.html',response_data={'Status':'An error occurred while handling the request.'})

        elif(request_type=='POST'):   
            data = json.dumps(form_data)
            #print(data)
            try:
                resp = requests.post(link,headers=header,data=data)
                return render_template('requestFor.html',response_data=resp.json())
            except(requests.exceptions.JSONDecodeError):
                return render_template('requestFor.html',response_data={'Status':'An error occurred while handling the request.'})
    else:
         return render_template('requestFor.html',response_data=None)