from django.db import models

# Create your models here.




class CustEnquiry(models.Model):
    custid = models.AutoField(primary_key=True,
                                serialize=False,
                                verbose_name='ID')
    name = models.CharField(max_length=25)
    telephone = models.CharField( max_length=10)
    email = models.EmailField(max_length=50)
    socialmedia = models.CharField( max_length=155)
    formal_education = models.CharField( max_length=50)


