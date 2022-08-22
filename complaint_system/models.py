import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.




class UserInfo(models.Model):
    USER_ROLE_CHOICE = [
        ('c', 'customer'),
        ('a', 'admin')
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=225)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20,choices=USER_ROLE_CHOICE, default=('c'))
    
    def __str__(self):
        return f'{self.id}-{self.email}'

class Ticket(models.Model):
    TICKET_STATUS_CHOICE = [
        ('p','pending'),
        ('c','complete'),
        ('ip','inprogress')
    ]
    # ticket_no = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=225)
    complaint = models.TextField()
    ticket_status = models.CharField(max_length=20,choices=TICKET_STATUS_CHOICE, default=('p'))

    def __str__(self):
        return f'{self.id}-{self.email}'