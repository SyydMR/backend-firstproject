from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class Country(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

class City(models.Model):
    name = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True) # Foreign key
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

class Corporation(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

class Transportation(models.Model):
    name = models.CharField(max_length=255)
    seat_count = models.IntegerField(default=25)

    corporation_id = models.ForeignKey(Corporation, on_delete=models.SET_NULL, null=True) # Foreign key
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

class Destination(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) # Foreign key
    description = models.TextField()
    img = models.ImageField(upload_to='destination_images/', default='destination_images/no_img.jpg')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return f"#{self.id} {self.city_id.name}"

    # def snippets(self):
    #     return self.description[:100] + '...'


class Destination_City(models.Model):
    """
    This shows the relation between destination and city to show the origin of the journey
    """
    destination = models.ForeignKey(to=Destination, on_delete=models.CASCADE)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    transportation = models.ForeignKey(to=Transportation, on_delete=models.CASCADE, blank=True, null=True, default=None)
    cost = models.BigIntegerField(default=0)
    

class Invoice(models.Model):
    date_origin = models.DateTimeField()
    count = models.IntegerField(null=False, default=1)

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Foreign key
    transportation_id = models.ForeignKey(Transportation, on_delete=models.SET_NULL, null=True) # Foreign key
    destination_id = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True) # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return 'factor ' + str(self.id)



class NationalCodes(models.Model):
    national_code = models.CharField(max_length=255, null=True)
    seat = models.CharField(max_length=255, null=True)

    invoice_id = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True) # Foreign key
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return 'national code ' + str(self.id)


class Destination_User(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Foreign key
    destination_id = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True) # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.destination_id, self.user_id)


class Comment(models.Model):
    message = models.TextField()
    title = models.CharField(max_length=255)
    ref_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, default=None) # Foreign key
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default='self') # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.id, self.title)

