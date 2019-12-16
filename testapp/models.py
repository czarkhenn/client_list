from django.db import models

optional = {
    "null":True,
    "blank":True

}

class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True)
    address_street_name = models.CharField(max_length=50, **optional)
    address_suburb = models.CharField(max_length=50, **optional)
    address_post_code = models.CharField(max_length=5, **optional)
    address_state = models.CharField(max_length=2, **optional)
    contact_name = models.CharField(max_length=50, **optional)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.client_name)