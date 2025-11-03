from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


# Helper tables
class Skill(models.Model): # optional skills for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)
class Interest(models.Model): # optional interests for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)

# Main tables
class User(models.Model):
    # Essential
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True)
    username=models.CharField(max_length=35, unique=True)
    displayname=models.CharField(max_length=35)

    VISIBILITY_CHOICES = [ # Can add more later if needed
            ("public", "Public"),
            ("private", "Private"),
    ]
    visibility = models.CharField(
            max_length=10,choices=VISIBILITY_CHOICES,default="public",db_index=True
    )

    # EXTREMELY IMPORTANT
    xp = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(500))
    xpneeded = models.IntegerField(default=100)

    # Optional
    school = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    grad_year = models.PositiveSmallIntegerField(null=True, blank=True, 
            validators=[MinValueValidator(2015), MaxValueValidator(2080)],
            db_index=True,
            help_text="4-digit grad year (e.g. 2028)"
    )

    # Socials
    discord = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    #Information
    bio = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="users")
    interests  = models.ManyToManyField(Interest,  blank=True, related_name="users")
    blocked = models.JSONField(default=list)

    # Extra info
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"] # ordered by oldest to newest

    def __str__(self): #how this table is visualized as plain text
        return f"{self.email} ({self.uuid})"
    
