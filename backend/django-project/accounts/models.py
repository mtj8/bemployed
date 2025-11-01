from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


# Helper tables
class Skill(models.Model): # optional skills for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)
class Role(models.Model): # optional roles for the user (e.g. backend, frontend, etc)
    name = models.CharField(max_length=25, unique=True, db_index=True)
class Interest(models.Model): # optional interests for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)

# Main tables
class User(models.Model):
    # Essential
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=254, unique=True)
    visibility = models.BooleanField(default=True)
    # Optional
    school = models.CharField(max_length=100, blank=True, null=True)
    grad_year = models.PositiveSmallIntegerField(null=True, blank=True, 
            validators=[MinValueValidator(2015), MaxValueValidator(2080)]
    )
    # Socials
    discord = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    #Information
    bio = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="students")
    roles  = models.ManyToManyField(Role,  blank=True, related_name="students")
    interests  = models.ManyToManyField(Interest,  blank=True, related_name="students")
