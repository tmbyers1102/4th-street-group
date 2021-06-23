from django.db import models
from django.utils import timezone
from django.urls import reverse


PROGRESS_CHOICES = (
    (0, 0),
    (25, 25),
    (50, 50),
    (75, 75),
    (100, 100),
)

# TECH_CHOICES = (
#     ('Django', 'Django'),
#     ('Django REST Framework', 'Django REST Framework'),
#     ('React', 'React'),
#     ('API', 'API'),
#     ('JavaScript', 'JavaScript'),
#     ('Stripe', 'Stripe'),
#     ('AWS S3', 'AWS S3'),
#     ('Bootstrap 4', 'Bootstrap 4'),
#     ('Tailwind', 'Tailwind'),
#     ('HTML', 'HTML'),
#     ('CSS', 'CSS'),
#     ('Python', 'Python'),

# )

# REQ_CHOICES = (
#     ('Database Backend', 'Database Backend'),
#     ('API', 'API'),
#     ('Full-Stack', 'Full-Stack'),
#     ('eCommerce', 'eCommerce'),
#     ('Facial Recognition', 'Facial Recognition'),
#     ('Subscription Billing', 'Subscription Billing'),
#     ('Kinetic Email', 'Kinetic Email'),
#     ('User Account', 'User Account'),
#     ('User Analytics', 'User Analytics'),
#     ('Fantasy Sports', 'Fantasy Sports'),
#     ('Product Marketplace', 'Product Marketplace'),
# )

class Requirement(models.Model):
    requirement_title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.requirement_title


class Tech(models.Model):
    tech_title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.tech_title


# This is the main model for this web app.
class Project(models.Model):
    title = models.CharField(max_length=100)
    title_slug = models.SlugField(blank=True, primary_key=True)
    description = models.TextField()
    market = models.TextField(blank=True, null=True, )
    url = models.URLField(blank=True)
    project_screenshot = models.ImageField(default='default_screenshot.jpg', upload_to='project_screenshots')
    project_logo = models.ImageField(blank=True, default='default_logo.jpg', upload_to='project_logos')
    date_posted = models.DateTimeField(default=timezone.now)
    active_project = models.BooleanField(default=False)
    github_url = models.URLField(blank=True)
    progress = models.IntegerField(choices=PROGRESS_CHOICES, default=0)
    card_logo = models.ImageField(blank=True, null=True, upload_to='card_logos')
    requirements = models.ManyToManyField(Requirement, blank=True)
    tech_used = models.ManyToManyField(Tech, blank=True)

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


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    # old phone style imported
    # phone = PhoneField(blank=True, help_text='Contact phone number')
    company = models.CharField(max_length=100, blank=True, null=True)
    interested_service = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web_app-home')


class Log(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.project, self.title)