from django.db import models

# Create your models here.


class Github(models.Model):
	githubuser = models.CharField(max_length=1000)
	imagelink = models.CharField(max_length=1000)
	username = models.CharField(max_length=1000)


	def _str_(self):
		return self.githubuser