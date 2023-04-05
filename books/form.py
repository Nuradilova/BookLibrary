from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Not selected'
        self.fields['publisher'].empty_label = 'Not selected'

    class Meta:
        model = Books
        fields = '__all__'


class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields = '__all__'

