from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Compound(models.Model):
    compound_id = models.CharField(max_length=30, primary_key=True)
    compound_name = models.CharField(max_length=30, default='')
    features = models.TextField(default='')

    def __str__(self):
        return self.compound_name

class Protein(models.Model):
    protein_id = models.CharField(max_length=30, primary_key=True)
    protein_name = models.CharField(max_length=30, default='')
    compounds = models.ManyToManyField(Compound, through='ProteinCompound')

    def __str__(self):
        return self.protein_name

class ProteinCompound(models.Model):
    protein_id = models.ForeignKey(Protein, on_delete='models.CASCADE')
    compound_id = models.ForeignKey(Compound, on_delete='models.CASCADE')
    activity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}-{}".format(self.protein_id, self.compound_id)

class Poll(models.Model):
    compound_name = models.CharField(max_length=30, default='')
    compound_id = models.CharField(max_length=30)
    features = models.TextField(default='')
    protein_name = models.CharField(max_length=30, default='')
    protein_id = models.CharField(max_length=30)
    date = models.DateField(default=date.today)

    def __str__(self):
        return "Your target protein {} (id: {}) and the drug compound {} (id: {})".format(self.Protein.name, self.Protein.protein_id, \
                self.Compound.name, self.Compound.compound_id)
