from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from pharma.contact.forms import ContactForm
from pharma.models.contact import Contact

def contact(request):
    """
    Handles the contact form submission.
    On POST, validates the form, saves the data to the database,
    and redirects to the success page.
    On GET, renders the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # save the form data to the database
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # send an email to the contact
            """send_mail(
                'Thank you for contacting us',
                'We have received your message and will get back to you soon.',
                'pharma@example.com',
                [email],
                fail_silently=False,) """
            # Redirect to the success page
            return redirect('pharma:success')
    else:
        form = ContactForm()
    return render(request, 'pharma/contact.html', {'form': form})

def success(request):
    """
    Renders the success page after a successful contact form submission.
    """
    message = 'Thank you for contacting us!'
    return render(request, 'pharma/success.html', {'message': message})