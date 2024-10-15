from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KG')
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple', null=True, blank=True)



class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.country_name}'


class Director(models.Model):
    director_name = models.CharField(max_length=32, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    director_image = models.ImageField(upload_to='director_img/', null=True, blank=True)

    def __str__(self):
        return f'{self.director_name}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    actor_image = models.ImageField(upload_to='actor_img/', null=True, blank=True)

    def __str__(self):
        return f'{self.actor_name}'


class Janre(models.Model):
    janre_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.janre_name}'


class Movie(models.Model):
    Type_CHOICES = (
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
    )
    movie_name = models.CharField(max_length=50)
    year = models.DateField(null=True, blank=True)
    country = models.ManyToManyField(Country, )
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    janre = models.ManyToManyField(Janre)
    types = MultiSelectField(choices=Type_CHOICES, max_choices=30)


    movie_time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    movie_trailer = models.FileField(upload_to='movie_trailer/', null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_img/', null=True, blank=True)
    movie = models.FileField(upload_to='movie_film/', null=True, blank=True)
    STATUS_MOVIE = (
        ('pro', 'pro'),
        ('simple', 'simple'),
    )
    status_movie = models.CharField(max_length=10, choices=STATUS_MOVIE, default='simple', null=True, blank=True)

    def __str__(self):
        return f'{self.movie_name}'


class MovieLanguages(models.Model):
    language = models.CharField(max_length=32)
    video = models.FileField(upload_to='videos/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.language}'


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='moments')


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, )
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name='Рейтинг')
    parent = models.ForeignKey('self', related_name='relies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.stars} stars'



class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart =models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart} - {self.movie}'


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' {self.user} - {self.viewed_at}'