from django.shortcuts import render


from .models import Contact

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect

from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'reviewApp/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'reviewApp/about.html', {'title': 'About Us'})



def contact(request):
    return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})


def privacy_policy(request):
    return render(request, 'reviewApp/privacy_policy.html')

def terms(request):
    return render(request, 'reviewApp/terms.html')


def contact_view(request):
    if request.method == 'POST':
        print("Form submitted.")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the submitted data as a Contact model instance
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect('reviewApp-success') # Redirect to a success page
    return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def success_view(request):
    return render(request, 'reviewApp/success.html', {'title': 'Success'})



