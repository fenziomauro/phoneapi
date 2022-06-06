from django.db import models

class Phonebook(models.Model):
    phonebook_name = models.CharField(max_length=200)

    def __str__(self):
        return self.phonebook_name

class Contact(models.Model):
    contatc = models.ForeignKey(Phonebook, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=200)
    contact_surname = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_surname