from django.db import models
from accounts.models import CustomUser


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
        return "{}".format(self.id)

    # def snippets(self):
    #     return self.description[:100] + '...'









class Invoice(models.Model):
    date_origin = models.DateTimeField()
    count = models.IntegerField(null=False, default=1)

    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) # Foreign key
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) # Foreign key
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
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) # Foreign key
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
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) # Foreign key

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta: # generally
        ordering = ['created_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

