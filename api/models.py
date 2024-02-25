from django.db import models

# Create your models here.
class userLogin(models.Model):
    name=models.CharField(max_length=50,unique=True,blank=False)
    password=models.CharField(max_length=20,blank=False)
    is_user=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Entries(models.Model):
    to_name=models.ForeignKey(userLogin,limit_choices_to={'is_user':False},on_delete=models.CASCADE,related_name='to_entries')
    from_name=models.ForeignKey(userLogin,limit_choices_to={'is_user':True},on_delete=models.CASCADE,related_name='from_entries')
    signed=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    design=models.ImageField(upload_to="uploads")

