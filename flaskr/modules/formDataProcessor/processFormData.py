import re

def processForm(form_data:dict):
    request_type=form_data.pop('request_type')
    link = form_data.pop('link')
    headers={}
    keys=list(form_data.keys())
    vals=list(form_data.values())
    for i in range(len(keys)):
        if(re.match("^header.",keys[i])):
            headers[vals[i]]=form_data[vals[i]]
            k = keys.pop(i)
            v=vals.pop(i)
            i-=1
        if(re.match("^Data.",keys[i])):
            k=keys.pop(i)
            v=vals.pop(i)
            i-=1
    formData=dict(zip(keys,vals))
    return link,formData,headers,request_type