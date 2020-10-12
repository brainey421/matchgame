from django.db import models

class Prompt(models.Model):
    text = models.CharField(max_length=280)
    date = models.DateField()
    
    def __str__(self):
        return self.text

class Party(models.Model):
    def __str__(self):
        return self.id

class Person(models.Model):
    name = models.CharField(max_length=32)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
