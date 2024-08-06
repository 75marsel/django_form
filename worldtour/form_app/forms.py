from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        print(f"""
              Email: {self.cleaned_data['email']}
              message: {self.cleaned_data['age']}
              message: {self.cleaned_data['message']}
              """)