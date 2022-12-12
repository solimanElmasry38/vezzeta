from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Search(models.Model):
    citys = [
        ("alex","alex"),
        ("cairo","cairo"),
    ]
    spec = [
        ("soolid","soolid"),
        ("cardef","cardef"),
        ("ssesf","ssesf"),
        ("sefg","sefg"),
        ("cardef","cardef"),
    ]
    DocName = models.CharField(null=True,max_length=15,blank=True)
    city = models.CharField(null=True,max_length=15,blank=True,choices=citys)
    specialization = models.CharField(null=True,max_length=15,blank=True,choices=spec)

    def __str__(self):
        return self.DocName


class Add(models.Model):
    Location=models.CharField(blank=True,null=True,max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    weatingHours=models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    workingHours=models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img= models.ImageField(default='def.png',upload_to='uplaoad')
    phone = models.IntegerField(blank=True, null=True,default=1)
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def CreateProfile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    

