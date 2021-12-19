from django import forms
from django.contrib.auth.models import User
from collector_app.models.collection import Collection

class CollectionForm(forms.ModelForm):
    collected_item = forms.CharField(required=True,  widget=forms.TextInput(attrs={'class':'form-control',  'id':'input-text'}))
    
    class Meta:
        model = Collection
        fields = ['collected_item']
