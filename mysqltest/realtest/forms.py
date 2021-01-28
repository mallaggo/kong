from django import forms
import datetime

from django.forms import SelectDateWidget

from .models import Image,Test,Product,Pcomment,Category


class RstForm(forms.Form):

    subject = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    summary = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!",
                'cols': 10, 'rows': 10
            })
    )
   # upload_date=forms.DateField(initial=datetime.date.today)
    upload_date=forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    #image = forms.ImageField(label=('Company Logo'), required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)
    image=forms.ImageField()
    #sender = forms.EmailField(help_text='A valid email address, please.')

    METHOD = (
        ('C', 'cash'),
        ('B', 'card'),
        ('P', 'point'),
    )
    acount = forms.CharField(label='What is your bill?', widget=forms.Select(choices=METHOD))

    """class Meta: #이 방식은 fields를 지정해 줘야 한다.
        model = Test
        fields = ('subject', 'image','summary','upload_date','acount')"""  #forms.Form 을 상속했기에 meta는 필요없다.
    #하지만, forms.Form 을 상속했기에 일일이 widget을 지정해야 한다.



class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta: #이 방식은 fields를 지정해 줘야 한다.
        model = Image
        fields = ('title', 'image')


class ProductForm(forms.ModelForm):
    """serial_number = forms.CharField()
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!",
                'cols': 10, 'rows': 10
            })
    )
    # image = forms.ImageField(label=('Company Logo'), required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)
    image = forms.ImageField()
    # sender = forms.EmailField(help_text='A valid email address, please.')
    price=forms.IntegerField()
    """
    class Meta:
        model=Product
        fields=('serial_number','name','image','content','price','categories')

class PcommentForm(forms.ModelForm):
    class Meta:
        model=Pcomment
        fields=('name','content')

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'size': 20,
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
