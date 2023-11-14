from django.db import models

# Create your models here.
class table(models.Model):
    nam=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self):
        return self.nam

class people(models.Model):
    na=models.CharField(max_length=250)
    im=models.ImageField(upload_to='pics')
    ab=models.TextField()