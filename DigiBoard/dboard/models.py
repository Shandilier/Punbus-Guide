from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import datetime, timedelta, time
today = datetime.now().date()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())


# Create your models here.

class Search(models.Model):
	user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	source = models.IntegerField()
	des = models.IntegerField()
	HH = models.IntegerField()
	MM = models.IntegerField()
	
	xm=models.IntegerField(null=True)
	am=models.IntegerField(null=True)
	bm=models.IntegerField(null=True)
	cm=models.IntegerField(null=True)
	dm=models.IntegerField(null=True)
	em=models.IntegerField(null=True)
	fm=models.IntegerField(null=True)
	gm=models.IntegerField(null=True)

	# timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	# def __str__(self):
	# 	return str(self.source)

# class UserProfile(models.Model):
# 	user=models.OneToOneField(User)
# 	first_name=models.CharField(max_length=200)
# 	last_name=models.CharField(max_length=200)
# 	avatar=models.FileField(null=True,blank=True)

# 	class Meta:
# 		db_table='UserProfile'
# 		ordering=['user_id']

# 	def get_url(self):
# 		return reverse('user-detail',args=[str(self.id)])

# 	def __str__(self):
# 		return self.user.username

# def create_profile(sender, **kwargs):
# 	if kwargs['created']:
# 		user_profile=UserProfile.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile,sender=User)
