from flaskr.modules.formDataProcessor.processFormData import processForm

some_data= {'request_type': 'GET', 'link': 'http://localhost:8080/message', 'headerKey0': 'Content-type', 'Content-type': 
'application/json', 'DataKey0': 'x-api-key', 'x-api-key': 'asdfasd', 'DataKey1': 'dbUserName', 'dbUserName': 'postgres'}

print(processForm(some_data))