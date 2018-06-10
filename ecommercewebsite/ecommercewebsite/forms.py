from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder" :"Enter Name","id":"exampleInputUsername"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email id","id":"exampleInputEmail"}))
    telephone=forms.CharField(max_length=10,min_length=10,widget=forms.TextInput(attrs={"placeholder":"Enter 10-digit mobile no.","class":"form-control","id":"telephone"}))
    description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"description", "placeholder":"Enter Your Message"}))
