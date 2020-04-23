from django.db import models

# Create your models here.

class House(models.Model):
	transaction_date = 	models.DateField()
	age = models.DecimalField(decimal_places=1, max_digits=10, default=2.2)
	mrt_station = models.DecimalField(decimal_places=5, max_digits=10, default = 1.2)
	convenience_stores = models.IntegerField(default = 1)
	latitude = models.DecimalField(decimal_places=5, max_digits=10, default = 1.2020)
	longitude = models.DecimalField(decimal_places=5, max_digits=10, default = 2.2020)
	price = models.DecimalField(decimal_places=5, max_digits=10, default = 2.2020)
