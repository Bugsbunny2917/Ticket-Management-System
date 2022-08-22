from typing import OrderedDict
from django.shortcuts import redirect, render, HttpResponse

from .serializer import Serializer
from .models import UserInfo, Ticket
from .serializer import Serializer
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Create your views here.
def login(request):
    # data =  request.GET('https://randomuser.me/api/?results=4').json()
    # print(data)
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def ticket(request):
    return render(request, 'complaint.html')

def admin_page(request):
    return render(request, 'admin.html')

def admin_registration(request):
    return render(request, 'admin registration.html')

def user_registration(request):
    # print("submit press function called")
    full_name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    role = request.POST.get('role')
    print(full_name,email,password, role)
    user = UserInfo(full_name = full_name, email = email, password = password, role = role)
    user.save()

    # return render(request, 'login.html')
    if role == 'c':
        return render(request, 'login.html')
    elif role == 'a':
        return render(request, 'admin.html')
    # return render(request, 'login.html')

def user_login(request):
    # print("submit press function called")
    # full_name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # role = request.POST.get('role')
    print(email,password)
    ticket_data = Ticket.objects.all()
    user_objs = UserInfo.objects.all()
    serializer = Serializer(user_objs, many=True)
    # print(dict(serializer.data[0]))
    for n in range(len(serializer.data)):
        print(dict(serializer.data[n]))
        if dict(serializer.data[n])['email'] == email:
            if dict(serializer.data[n])['role'] == 'c':
                if dict(serializer.data[n])['password'] == password:
                    return render(request, 'user dash.html', 
                    {'ticket_data' : ticket_data})
                else:
                    return HttpResponse('Wrong password')
            else:
                return HttpResponse('Invalid User ID')

        else:
            return HttpResponse('Invalid User Email')
    print(user_objs)
    # print(rows)
    # return render(request, 'user dash.html', 
    # {'ticket_data' : ticket_data})

def admin_login(request):
    # print("submit press function called")
    # full_name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # role = request.POST.get('role')
    ticket_data = Ticket.objects.all()
    user_objs = UserInfo.objects.all()
    serializer = Serializer(user_objs, many=True)
    # print(dict(serializer.data[0]))
    for n in range(len(serializer.data)):
        print(dict(serializer.data[n]))
        if dict(serializer.data[n])['email'] == email:
            if dict(serializer.data[n])['role'] == 'a':
                if dict(serializer.data[n])['password'] == password:
                    return render(request, 'user dash.html', 
                    {'ticket_data' : ticket_data})

                else:
                    return HttpResponse('Wrong password')

            else:
                return HttpResponse('Invalid User ID')

        else:
            return HttpResponse('Invalid User Email')
    print(email,password)
    return render(request, 'admin dash.html')

def complaint_ticket(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    complaint = request.POST.get('message')
    print(name, email, complaint)
    ticket = Ticket(name = name, email = email, complaint = complaint)
    ticket.save()
    return render(request, 'user dash.html')
