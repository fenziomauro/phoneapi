from django.shortcuts import render, get_object_or_404
from .models import Contact, Phonebook
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PhonebookSerializer, ContactSerializer





class IndexView(generic.ListView):
    template_name = 'phonebook/index.html'
    context_object_name = 'phonebooks'

    def get_queryset(self):
        return Phonebook.objects.order_by('phonebook_name')

def add(request):
    text=request.POST['phone']
    p = Phonebook(phonebook_name=text)
    p.save()
    response = "Phonebook %s created"
    return HttpResponse(response % text)

def addcontact(request, phonebook_id):
    phonebook = get_object_or_404(Phonebook, pk=phonebook_id)
    name = request.POST['new']
    surname = request.POST['surname']
    phone = request.POST['phone']
    phonebook.contact_set.create(contact_name=name, contact_surname=surname, contact_phone=phone)
    responce = "Contact %s created"
    return HttpResponse(responce % name)

class DetailView(generic.DetailView):
    model = Phonebook
    template_name = 'phonebook/detail.html'


class PhonebookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Phonebook.objects.all().order_by('phonebook_name')
    serializer_class = PhonebookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

