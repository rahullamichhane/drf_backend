from django.shortcuts import render,redirect
from .forms import ContactForm


# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'registration/contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')
    
    
