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
        # self.helper.add_input(Submit('submit', 'Save person'))