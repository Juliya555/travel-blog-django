from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
from .forms import SubscriberForm


def index(request):
    form = SubscriberForm
    places = Place.objects.all()
    return render(request, "index.html", locals())


def mail(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

        email = EmailMessage(
            subject="Hello Travel: 7 best cities to visit",
            body="Hello. Please, enjoy our top 7 world's best cities to visit!",
            from_email=settings.EMAIL_HOST_USER,
            to=[data["email"]],
        )
        email.attach_file("static/mail_documents/7_cities_to_visit.pdf")
        email.send()

    return render(request, "mail_received.html", locals())


