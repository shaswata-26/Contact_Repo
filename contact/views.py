
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            form = ContactForm()  # Clear the form after saving
            return HttpResponse("Thank you for your message!")  # Display success message
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})



def getData(request):
     if request.method == 'GET':
        data = Contact.objects.all();
        return render(request, 'list.html', {'data': data})
