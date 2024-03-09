import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# views.py

from django.http import JsonResponse
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import JsonResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json
# views.py

from io import BytesIO
import base64

# views.py

# views.py
def page1_view(request):
    return render(request, 'myApp/graphco.html')

def my_function(request):
    # Your function logic here
    return send_email()

def send_email(request):
    #     recipient_list = request.POST.get('to_email')
    
    try:
        message = '''🚨 ALERT: 🌍 ENVIRONMENTAL HAZARD DETECTED 🚨

Attention all! The environment poses a significant threat to your health! 🌿🚫 High pollution levels can lead to severe respiratory issues, cardiovascular problems, and other health complications. It's crucial to take immediate action to protect yourself and your loved ones.

🛑 Avoid prolonged exposure to polluted air and contaminated water sources.
💊 If experiencing symptoms such as difficulty breathing, chest pain, or dizziness, seek medical attention promptly.
🌱 Support initiatives to reduce emissions, conserve resources, and promote sustainable living practices to mitigate environmental hazards.

Your health and well-being are paramount. Act now to safeguard yourself against environmental risks and ensure a healthier future! 🛡 #ProtectYourHealth #EnvironmentalAwareness #CleanAir #CleanWater'''
        subject = 'Environmental Issues Detected'
        from_email = 'enter-your-email'
        recipient_list = []
        recipient_list.append(email)

        # recipient_list = ['dassiananya@gmail.com']  # Update with actual recipient email address

        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}', status=500)
  


def login_page(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            global email
            email = user.email 
            # Redirect to the next page with email in the query string
            redirect_url = reverse('image_line') 
            return HttpResponseRedirect(redirect_url)
        else:
            error_message = "Invalid username or password"

    return render(request, 'myApp/login.html', {'error_message': error_message})



def check_readings_page(request):
     email = request.GET.get('email')
     return render(request, 'myApp/image_line.html', {'email': email})


def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already associated with an account.')
            else:
                form.save()
                return redirect('login')
    else:
        print("error")
        form = SignUpForm()
    return render(request, 'myApp/signup.html', {'form': form})

def image_line_page(request):
    return render(request, 'myApp/login.html')

def problemsTable(request):
    return render(request, 'myApp/problemsTable.html')

def communityTable(request):
    return render(request, 'myApp/communityTable.html')

# def home(request):
#     return HttpResponse("Hello, Django!")

# def hello_there(request, name):
#     print(request.build_absolute_uri()) #optional
#     return render(
#         request,
#         'myApp/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)