from django import forms
from .models import Posts

class CategoryForm(forms.Form):
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class AuthorForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile_No = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('created_at','updated_at',)
        widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(),
            'image':forms.ImageField(),
        #    'created_at':forms.DateTimeField(),
        #    'updated_at':forms.DateTimeField()
        }


class BlogSearch(forms.Form):
    Search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))