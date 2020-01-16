from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template


def emailView(request):
    template_name = 'contact.html'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['pharmacy.uz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact:success')
    return render(request, template_name, {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
