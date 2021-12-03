from django.db import models

# Create your models here.



class MenuItem(models.Model):
	CATEGORY_CHOICES = (
		('food', 'food'),
		('beverage', 'beverage'),
	)

	SUB_CATEGORY_CHOICES = (
		('vegetables', 'vegetables'),
		('sweet', 'sweet'),
		('fruit', 'fruit'),
		('cold-drink', 'cold-drink'),
		('coffee', 'coffee'),
	)

	name = models.CharField(max_length=100, blank=True, null=True)
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
	subcategory = models.CharField(max_length=50, choices=SUB_CATEGORY_CHOICES, blank=True, null=True)
	description = models.CharField(max_length=300, blank=True, null=True)
	price = models.FloatField(default=0.0)

	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)