from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
	MAX_LEN = 30
	name = models.CharField(max_length=MAX_LEN)
	location = models.CharField(max_length=MAX_LEN)
	date_created = models.DateTimeField(default=timezone.now)
	date_approved = models.DateTimeField(blank=True, null=True)
	developer = models.CharField(max_length=MAX_LEN)
	rating = models.IntegerField(default=0);
	project_status = models.ForeignKey(ProjectStatus)
	banner = models.ImageField(upload_to= settings.SHARE_IMAGE_UPLOAD_PATH)
	completion_date = models.DateTimeField(blank=True, null=True)
	other_details = models.CharField(max_length=MAX_LEN*20)
	project_type = models.ForeignKey(ProjectType)
	
class ProjectType(models.Model):
	project_type_name = models.CharField(max_length=MAX_LEN)
	
class ProjectStatus(models.Model):
	project_status_name = models.CharField(max_length=MAX_LEN)

class UnitModel(models.Model):
	project = models.ForeignKey(Project):
	date_created = models.DateTimeField(default=timezone.now)
	date_approved = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=MAX_LEN)
	lot_area = models.IntegerField(default=0)
	floor_area = models.IntegerField(default=0)
	unit_type = models.ForeignKey(UnitTypes)
	price = models.IntegerField(default=0)
	other_details = models.CharField(max_length=MAX_LEN)
	reservation = models.IntegerField(default=0)

class UnitTypes(models.Model):
	unit_type_name = models.CharField(max_length=MAX_LEN)
	
class Gallery(models.Model):
	unit_model = models.ForeignKey(UnitModel)
	project = models.ForeignKey(Project)
	image = models.ImageField(upload_to=settings.SHARE_IMAGE_UPLOAD_PATH)
	caption = models.CharField(max_length=MAX_LEN)
	
class AgentProfile(models.Model)
	name = models.charField(max_lenth=MAX_LEN*2)
	date_started = models.DateTimeField()
	status = models.ForeignKey(AgentStatus)
	profile_pic = models.ImageField(upload_to=settings.SHARE_IMAGE_UPLOAD_PATH)
	#email
	#contact no
	#license no
	about = models.CharField(max_length=MAX_LEN*3)
	

	
	