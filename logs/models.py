from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    email = models.EmailField()


class DepartmentRole(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

	
	