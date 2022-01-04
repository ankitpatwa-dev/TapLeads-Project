from django.db import models
from django.contrib.auth.models import User



class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contact_type=models.CharField(max_length=200, null=True)
	full_name=models.CharField(max_length=200, null=True)
	first_name=models.CharField(max_length=200, null=True)
	middle_name=models.CharField(max_length=200, null=True)
	last_name=models.CharField(max_length=200, null=True)
	company=models.CharField(max_length=200, null=True)
	designation=models.CharField(max_length=200, null=True)
	emailid_primary=models.EmailField(max_length=200, null=True)
	emailid_secondary=models.EmailField(max_length=200, null=True)
	aadhar=models.CharField(max_length=12, null=True)
	pan_card=models.CharField(max_length=10, null=True)
	phone=models.CharField(max_length=10, null=True)
	current_location=models.CharField(max_length=200, null=True)
	preferred_location=models.CharField(max_length=200, null=True)
	gender=models.CharField(max_length=10, null=True)
	title=models.CharField(max_length=200, null=True)
	department=models.CharField(max_length=200, null=True)
	university=models.CharField(max_length=200, null=True)
	degree=models.CharField(max_length=200, null=True)
	passing_year=models.CharField(max_length=200, null=True)
	college=models.CharField(max_length=200, null=True)
	linkedin=models.URLField(null=True)
	facebook=models.URLField(null=True)
	instagram=models.URLField(null=True)
	industry=models.CharField(max_length=200, null=True)
	country=models.CharField(max_length=200, null=True)
	state=models.CharField(max_length=200, null=True)
	pin_code=models.CharField(max_length=200, null=True)
	key_skills=models.CharField(max_length=200, null=True)
	total_experience=models.CharField(max_length=200, null=True)
	years_in_business=models.CharField(max_length=200, null=True)
	cin_no=models.CharField(max_length=200, null=True)
	turnover=models.CharField(max_length=200,default="0", null=True)
	date_of_incorporation=models.CharField(max_length=200,null=True)
	employees=models.CharField(max_length=200, null=True)
	ctc=models.CharField(max_length=200, null=True)
	notes=models.CharField(max_length=200, null=True)
	remarks=models.CharField(max_length=200, null=True)
	status=models.CharField(max_length=200, null=True)
	notice_period=models.CharField(max_length=200, null=True)



class SaveSearch(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	search_criteria=models.CharField(max_length=200)

	def __str__(self):
		return f"{self.user} | {self.search_criteria}"


class View(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contact=models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)

	def __str__(self):
             return "%s -> %s" % (self.user_id, self.contact_id)

class Score(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	value = models.IntegerField(default=0)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)

class Method(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    type=models.CharField(max_length=10, default="predefined")
    name=models.CharField(max_length=200)

class Field(models.Model):
    method=models.ForeignKey(Method, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    weightage=models.IntegerField(default=0)


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, null=True)
    total_limits=models.IntegerField(default=0)
    viewed=models.IntegerField(default=0)
    current_method=models.ForeignKey(Method, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.total_limits)



