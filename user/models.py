from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Contact(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name
class Service(models.Model):
    Email = models.EmailField(max_length=100)
    desc = models.TextField()
    def __str__(self):
        return self.desc



class Cotegories(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    



class Post(models.Model):
        title = models.CharField(max_length=100)
        # auther = models.ForeignKey(Cotegories , on_delete=models.CASCADE)
        body= models.TextField()
        # images = models.ImageField(upload_to='profile_pics',default='default.jpeg')
        pst = models.ImageField(default= 'default.jpg',upload_to='upload_pics')
        def __str__(self):
            return  self.title +'-'
            # + str(self.autherr) + self.image
        def get_absolute_url(self):
            return reverse('articledetail',args=(str(self.id)))



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    # auther = models.ForeignKey(User , on_delete=models.CASCADE)
    # category = models.Foreignkey(Cotegories , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to='profile_pics')
    image2 = models.ImageField(default='default.jpeg',upload_to='profile_pics')
    image3 = models.ImageField(default='default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


