from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''
    <h1>Hello Zuri!</h1>
    <p>
    My Name is Olabanji MAyowa Emmanuel
    I'm learning python with django with Zuri & I4G
    </p>
    ''')