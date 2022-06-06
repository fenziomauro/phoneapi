from rest_framework import serializers
from .models import Phonebook, Contact


class PhonebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phonebook
        fields = ['id', 'phonebook_name','contact_set']
        depth = 1


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'contact_name','contact_surname', 'contact_phone']