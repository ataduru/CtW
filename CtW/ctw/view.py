# View functions

from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import simplejson as json
import sys, os, pickle, objects, time
import pickle
from ser import *


#us = User.objects.get(username='ata')
#us.delete()

socket_list = []


def success(obj, name, idno):
	return HttpResponse(json.dumps({'result':'Success', name : obj, 'id': kul.empire_no, 'ad' : (objects.dicts[`idno`].ad), 'coin' : objects.dicts[`idno`].coin, 'ed' : objects.dicts[`idno`].sinir_savunmasi, 'wood' : objects.dicts[`idno`].tahta_miktari, 'iron' : objects.dicts[`idno`].metal_miktari, 'as' : objects.dicts[`idno`].saldiri_askerleri.sayi, 'ds' : objects.dicts[`idno`].savunma_askerleri.sayi, 'asg' : objects.dicts[`idno`].saldiri_askerleri.saldiri_gucu, 'dsg' : objects.dicts[`idno`].savunma_askerleri.savunma_gucu }),
				'text/json')

def error(reason):
	return HttpResponse(json.dumps({'result':'Fail','reason' : reason}),
				'text/json')

def updateMap(request):

	while(1):

		command = 'command'

		if(os.stat("ctw/users.txt").st_size != 0):
			f = open("ctw/users.txt", "r+")
			geciciListe = ''.join(f.readlines())
			objects.users = pickle.loads(geciciListe)
			f.close()

		username = request.user.get_username()
		kul.empire_no = objects.users[str(username)]

		ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

		counter = 0		
		for sock in SOCKET_LIST:
			if (sock != SOCKET_LIST[0] and objects.empireIds[str(sock.getpeername())] == kul.empire_no):
				socket_list[counter-1].send(command)
			counter += 1
	
		if(kul.empire_no == objects.users[str(username)]):
			har = harita.showMap(kul.empire_no)

			return success(har, 'harita', kul.empire_no)	

def home(request):
	'''Home page of application, renders all movies on
	an HTML table.'''
	# this is longer version for authentication control
        # @login_required decorator does the same job

	if  not request.user.is_authenticated():
		return redirect("/login")

	try:
		# if there is a message, it is added
		context.update({'message': request.GET['msg']})
	except:
		pass
	return render(request, "home.html", context)


def login_view(request):
	'''Show login form'''
	
	context =  {'message':'Welcome'}
	return render(request, 'login.html', context)

def login_post(request):
	'''Login to system'''
	username = request.POST['username']
	password = request.POST['password']
	# check for authentication

	#logout(request)

	user = authenticate(username=username, password=password)

	if user is not None:
		# test if user is not disabled by admin		
		if user.is_active:
			login(request, user)
			updateMap(request)
			if(os.stat("ctw/users.txt").st_size != 0):
				f = open("ctw/users.txt", "r+")
				geciciListe = ''.join(f.readlines())
				objects.users = pickle.loads(geciciListe)
				f.close()
			eid = objects.users[str(user)]						
			f = open("empireid.txt", "r+")
			f.truncate()
			f.write(str(eid))
			f.close()
			kul.empire_no = eid
			return render(request, 'client.html', {'message':'', 'username':username})
			# create login session 
			
		else:
			return render(request, 'login.html', {'message':
						'Account is disabled'})
	else:

		# Return an 'invalid login' error message.
		return render(request, 'login.html', {'message':
						'Invalid username or password'})


def commands(request):

	command = request.POST['command']
	print command
	#return HttpResponse(command)
	if(os.stat("ctw/users.txt").st_size != 0):
		f = open("ctw/users.txt", "r+")
		geciciListe = ''.join(f.readlines())
		objects.users = pickle.loads(geciciListe)
		f.close()

	username = request.user.get_username()
	kul.empire_no = objects.users[str(username)]

	ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

	counter = 0		
	for sock in SOCKET_LIST:
		if (sock != SOCKET_LIST[0] and objects.empireIds[str(sock.getpeername())] == kul.empire_no):
			socket_list[counter-1].send(command)
		counter += 1

	time.sleep(1)
	
	har = harita.showMap(kul.empire_no)

	context = {'id': objects.users[str(username)], 'harita' : har, 'ad' : (objects.dicts[`objects.users[str(username)]`].ad), 'coin' : objects.dicts[`objects.users[str(username)]`].coin, 'ed' : objects.dicts[`objects.users[str(username)]`].sinir_savunmasi, 'wood' : objects.dicts[`objects.users[str(username)]`].tahta_miktari, 'iron' : objects.dicts[`objects.users[str(username)]`].metal_miktari, 'as' : objects.dicts[`objects.users[str(username)]`].saldiri_askerleri.sayi, 'ds' : objects.dicts[`objects.users[str(username)]`].savunma_askerleri.sayi, 'asg' : objects.dicts[`objects.users[str(username)]`].saldiri_askerleri.saldiri_gucu, 'dsg' : objects.dicts[`objects.users[str(username)]`].savunma_askerleri.savunma_gucu }  

	return render(request, 'command.html', context)


def sign_up_view(request):
	context =  {'message':''}
	return render(request, 'signup.html', context)

def sign_up(request):
	geciciListe = []
	geciciListe2 = []
	liste = []
	
	username = request.GET['username']
	password = request.GET['password']
	eid = request.GET['id']
	fname = request.GET['fname']
	lname = request.GET['lname']


	if(os.stat("ctw/usernames.txt").st_size != 0):
		f = open("ctw/usernames.txt", "r+")
		liste = ''.join(f.readlines())
		objects.usernames = pickle.loads(liste)
		f.close()

	if username in objects.usernames:
		return render(request, 'signup.html', {'message':'Username is already taken.'})

	if(os.stat("ctw/users.txt").st_size != 0):
		f = open("ctw/users.txt", "r+")
		geciciListe = ''.join(f.readlines())
		objects.users = pickle.loads(geciciListe)
		f.close()

	if(os.stat("ctw/id.txt").st_size != 0):
		f = open("ctw/id.txt", "r+")
		geciciListe2 = ''.join(f.readlines())
		objects.mp_empire_id = pickle.loads(geciciListe2)
		f.close()

	if int(eid) not in objects.mp_empire_id:
		return render(request, 'signup.html', {'message':'ID is not available'})

	objects.usernames.append(username)
	objects.mp_empire_id.remove(int(eid))
	objects.users[str(username)] = int(eid)

	f = open("ctw/usernames.txt", "r+")
	f.truncate()
	f.write(pickle.dumps(objects.usernames))
	f.close()


	f = open("ctw/empireid.txt", "r+")
	f.truncate()
	f.write(str(eid))
	f.close()


	f = open("ctw/users.txt", "r+")
	f.truncate()
	f.write(pickle.dumps(objects.users))
	f.close()

	f = open("ctw/id.txt", "r+")
	f.truncate()
	f.write(pickle.dumps(objects.mp_empire_id))
	f.close()

	User.objects.create_user(username=username, email=eid, password=password)

	'''if user is not None:'''

	return render(request, 'login.html')
	


def logout_view(request):
	'''Simply logout'''

	counter = 0

	for sock in SOCKET_LIST:
		if (sock != SOCKET_LIST[0] and objects.empireIds[str(sock.getpeername())] == kul.empire_no):
			sil = sock.getpeername()
		counter += 1

	del socket_list[-1]
	del SOCKET_LIST[counter-1]
	del objects.empireIds[str(sil)]

	logout(request)

	return redirect("/login")

def client(request):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	host = ''
	port = 9009

	s.settimeout(2)

	# connect to remote host
	#try :
	s.connect((host, port))
	socket_list.append(s)
	user = request.user.get_username()
	if(os.stat("ctw/users.txt").st_size != 0):
		f = open("ctw/users.txt", "r+")
		geciciListe = ''.join(f.readlines())
		objects.users = pickle.loads(geciciListe)
		f.close()
	eid = objects.users[str(user)]
	
	har = harita.showMap(eid)

	kul.empire_no = eid
	
	context = {'id': kul.empire_no, 'harita': har, 'ad' : (objects.dicts[`kul.empire_no`].ad), 'coin' : objects.dicts[`kul.empire_no`].coin, 'ed' : objects.dicts[`kul.empire_no`].sinir_savunmasi, 'wood' : objects.dicts[`kul.empire_no`].tahta_miktari, 'iron' : objects.dicts[`kul.empire_no`].metal_miktari, 'as' : objects.dicts[`kul.empire_no`].saldiri_askerleri.sayi, 'ds' : objects.dicts[`kul.empire_no`].savunma_askerleri.sayi, 'asg' : objects.dicts[`kul.empire_no`].saldiri_askerleri.saldiri_gucu, 'dsg' : objects.dicts[`kul.empire_no`].savunma_askerleri.savunma_gucu }  

	return render(request, 'command.html' , context)
	#except :
		#print 'Unable to connect'
		#sys.exit()



