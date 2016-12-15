from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save

# Create your models here.

class Strain(models.Model):
	user = models.ForeignKey(User)
	slug = models.SlugField(unique=True)
	name = models.CharField(max_length=150)
	initials = models.CharField(max_length=3)
	strain_type_choices = (
		('indica', 'Indica'),
		('sativa', 'Sativa'),
		('hybrid', 'Hybrid'),
	)
	strain_type = models.CharField(
		max_length=6,
		choices=strain_type_choices,
	)
	sleepy = models.IntegerField(
			default=1,
			validators=[
				MaxValueValidator(10),
				MinValueValidator(1)
			]
		)
	creative = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	hungry = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	giggles = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	relaxed = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	happy = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	pain = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	stress = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	insomnia = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	depression = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	lack_of_appetite = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	paranoia = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	cotton_mouth = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	dry_eyes = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	headache = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	eighth_price = models.IntegerField(
		default=0,
	)
	quarter_price = models.IntegerField(
		default=0,
	)
	half_price = models.IntegerField(
		default=0,
	)
	ounce_price = models.IntegerField(
		default=0,
	)
	description = models.TextField(blank=False)
	likes = models.IntegerField(default=0)
	image = models.ImageField(upload_to='strain_images', blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("/", kwargs={'slug': self.slug})

class Profile(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='profile_images', blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return self.first_name

class Comment(models.Model):
	author = models.ForeignKey(User)
	strain = models.ForeignKey('Strain', related_name="comments")
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	approved_comment = models.BooleanField(default=True)
	
	def approve(self):
		self.approved_comment = True
		self.save()
		
	def __str__(self):
		return self.text

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Strain.objects.filter(slug=slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug
	
def pre_save_strain_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	
pre_save.connect(pre_save_strain_receiver, sender=Strain)