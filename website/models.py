from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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

    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{}".format(self.id)


class Invoice(models.Model):
    date_origin = models.DateTimeField()
    date_destination = models.DateTimeField()
    seat = models.CharField(max_length=255)

    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) # Foreign key
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Foreign key
    transportation_id = models.ForeignKey(Transportation, on_delete=models.SET_NULL, null=True) # Foreign key
    destination_id = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True) # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return 'factor ' + self.id












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
    ref_id = models.IntegerField(default=0) # Foreign key
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

