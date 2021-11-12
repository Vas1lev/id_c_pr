from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

from base.mychoice import dep_choice, desc_choices, gen_choice


class Info(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    citizenship = models.CharField(max_length=3, default='GEO', editable=False)
    gen = models.CharField(max_length=10, blank=False, null=False, choices=gen_choice, default="gen choice")
    department = models.CharField(max_length=60, blank=False, null=False, choices=dep_choice, default="dep choice")
    personal_no = models.CharField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{1,11}$')])
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    date_of_expiry = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    signature = models.TextField(max_length=100, blank=False)
    card_no = models.CharField(max_length=9, blank=False)
    place_of_birth = models.CharField(max_length=100, blank=False)
    date_of_issue = models.DateTimeField(default=timezone.now)
    issuing_authority = models.TextField(max_length=400, blank=False)
    description = MultiSelectField(choices=desc_choices, max_length=80, default="description")
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='default.jpg')

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
