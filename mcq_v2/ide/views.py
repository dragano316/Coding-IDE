from django.shortcuts import render
import requests, json
# Create your views here.


# RUN_URL="https://api.judge0.com/?base64_encoded=true&wait=true"
COMPILE_URL="https://api.judge0.com/submissions/?base64_encoded=false&wait=true"



def ide(request):
	context={
		"bool":False,
		"source_code":"""#include &lt;stdio.h&gt;
void main(){
    /*your code goes here*/
}""",
	}
	if request.POST:
		code=request.POST.get('code_1')
		language_id=4
		rundata={
			'source_code':code,
			'language_id':language_id,
			'number_of_runs':1,
			'cpu_time_limit':2,
			'cpu_extra_time':0.5,
			'wall_time_limit':5,
			'memory_limit':128000,
			'stack_limit':64000,
			'max_processes_and_or_threads':30,
			'enable_per_process_and_thread_time_limit':False,
			'enable_per_process_and_thread_memory_limit':True,
			'max_file_size':1024,
			'stdin':None,
			'expected_output':"hello, \n",
			"token": "899ae152-2dc8-41a9-b6e5-69db3f1ab24a"
		}
		# COMPILE_URL=
		r = requests.post(COMPILE_URL, data=rundata)
		print(r.json())
		{'stdout': 'hello, \n', 'time': '0.001', 'memory': 128, 'stderr': None, 
		'token': '2e56b33a-1894-422f-80b9-1f867503b389', 'compile_output': None, 'message': None, 
		'status': {'id': 3, 'description': 'Accepted'}}

		context={
			"bool":True,
			"source_code":code,
			'stdout':r.get('stdout'),
			'time':r.get('time'),
			'memory':r.get('memory'),
			'stderr':r.get('stderr'),
			'token':r.get('token'),
			'compile_output':r.get('compile_output'),
			'message':r.get('message'),
			'status':r.get('status').get('description'),

		}
	return render(request,"ide/ide_home.html",context)
