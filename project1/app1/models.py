from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User             #django maintains a default DB of users

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default = timezone.now)
    post_content = models.TextField(default = "")

    def __str__(self):
        return self.title           #will show the title name in admin panel instead of "post object"
    

#create a baisc example model
class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

# One to Many
# One type of chai can have many reviews
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete = models.CASCADE)           #
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    

# Many to Many
# A store can have many chai varieties and vice versa
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety)

    def __str__(self):
        return self.name


# One to One
# A certificate is unique to a chai
class ChaiCert(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete = models.CASCADE)
    cert_num = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Cert for {self.chai.name}"