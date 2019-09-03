from django import forms
from .models import Poll
import csv

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('compound_id', 'compound_name', 'features', \
                  'protein_name', 'protein_id')

# class 
# class DataInput(forms.Form):
#     file = forms.FileField()
#
#     def save(self):
#         records = csv.reader(self.cleaned_data["file"])
#         for line in records:
#             input_data = Compound()
#             input_data.compound_id = line[0]
#             input_data.compound_name = 'C-' + str(input_data.compound_id)
#             input_data.compound_act = float(line[1])
#             input_data.features = ','.join(map(str, line[2:]))
#             input_data.save()
