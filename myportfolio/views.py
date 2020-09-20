from django.shortcuts import render

from django.contrib import messages
from myportfolio.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Message = request.POST.get('Message')
        contact = Contact(name = name, email = email, subject = subject, Message = Message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent. We contact you shortly!')
    return render(request, "index.html")

