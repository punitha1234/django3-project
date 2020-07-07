from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request, 'generator/home.html')
def password(request):
	l=list()
	if request.GET.get('lowercase'):
		l.extend(list('abcdefghijklmnopqrstuvwxyz'))
	if request.GET.get('uppercase'):
		l.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('numbers'):
		l.extend(list('0123456789'))
	if request.GET.get('specialcharacters'):
		l.extend(list('!@#$%^&*()'))
	length=int(request.GET.get('length'))			
	password=''
	for i in range(length):
		password+=(random.choice(l))
	return render(request, 'generator/password.html',{'password':password})
def about(request):
	return render(request,'generator/about.html')
