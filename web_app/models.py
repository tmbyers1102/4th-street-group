from django.db import models
from django.utils import timezone


# This is the main model for this web app.
class Project(models.Model):
    title = models.CharField(max_length=100)
    title_slug = models.SlugField(blank=True, primary_key=True)
    description = models.TextField()
    market = models.TextField()
    url = models.URLField(blank=True)
    project_screenshot = models.ImageField(default='default_screenshot.jpg', upload_to='project_screenshots')
    project_logo = models.ImageField(blank=True, default='default_logo.jpg', upload_to='project_logos')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# In order to make a photo gallery of each project's screengrabs, I had to make a new model and assign it to a project.
class Screengrab(models.Model):
    screen_grab = models.ImageField(default='default_project_screen_grab.jpg', upload_to='screen_grabs')
    # it was recommended online to add a 'related_name=' argument to the ForeignKey but I deleted it
    assigned_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100, default='Unassigned')

    def __str__(self):
        return self.identifier


class Requirement(models.Model):
    requirement_title = models.CharField(max_length=100, default='NA', blank=False)
    client_requirement = models.TextField()
    assigned_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.requirement_title