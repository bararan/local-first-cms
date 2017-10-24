from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

class Business(models.Model):
    BUSINESS_TYPES = (
        ('shopping', 'Shopping'),
        ('entertainment', 'Entertainment'),
        ('restaurants', 'Restaurants'),
        ('services', 'Services'),
    )
    name = models.CharField(max_length=100) #If this is too much/little we should modify
    slug = models.SlugField(max_length=100, unique=True)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES, default='shopping')
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    phone_validator = RegexValidator(regex=r'^[1-9]\d{9}$', message='Invalid phone number!')
    phone_number = models.CharField(max_length=10, validators=[phone_validator])
    email = models.EmailField()
    website = models.URLField(blank=True)
    social_fb = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
     # Add other social media links here if needed

    class Meta:
        ordering = ('name',)

    def _generate_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Business.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num +=1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_slug()
        super().save()

    def __str__(self):
        return self.name

class CalendarEvent(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.CharField(max_length=300)
    date_time = models.DateTimeField()
    description = models.CharField(max_length=500)
    photos = models.FilePathField()
    businesses = models.ManyToManyField(Business) #In case we want to show participating businesses

    class Meta:
        ordering = ('-date_time',)

    def _generate_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while CalendarEvent.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num +=1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_slug()
        super().save()

    def __str__(self):
        return self.title

class EventPicture(models.Model):
    file_path = models.FilePathField()
    event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)

    class Meta:
        ordering = ('file_path',)
