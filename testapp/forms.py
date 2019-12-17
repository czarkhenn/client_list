from crispy_forms.helper import FormHelper
from testapp.models import Client
from django import forms

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = fields = ('client_name', 'email', 'phone_number', 'address_street_name', 'address_suburb', 'address_post_code', 'address_state', 'contact_name')

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['email'].label = "Email Adress"
        self.fields['client_name'].label = "Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['address_street_name'].label = "Street Name"
        self.fields['address_suburb'].label = "Suburb"
        self.fields['address_state'].label = "State"
        self.fields['contact_name'].label = "Contact Name"
        self.fields['address_post_code'].label = "Postal Code"
