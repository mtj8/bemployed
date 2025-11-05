from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Helper tables
class Skill(models.Model): # optional skills for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)
    def __str__(self): 
        return f"{self.name}"

class Interest(models.Model): # optional interests for the user
    name = models.CharField(max_length=25, unique=True, db_index=True)
    def __str__(self): 
        return f"{self.name}"

# Main tables
class User(AbstractUser):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # use email for login
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Extra Fields
    first_name = models.CharField(max_length=35, blank=True)
    last_name = models.CharField(max_length=35, blank=True)

    VISIBILITY_CHOICES = [ # Can add more later if needed
            ("public", "Public"),
            ("private", "Private"),
    ]

    visibility = models.CharField(
            max_length=10,choices=VISIBILITY_CHOICES,default="public",db_index=True
    )

    # Expereince/Levels
    xp = models.PositiveSmallIntegerField(default=0,
        validators=[MaxValueValidator(500)]
    )    
    level = models.PositiveSmallIntegerField(default=0,
        validators=[MaxValueValidator(500)]
    )
    xpneeded = models.PositiveSmallIntegerField(default=100,
        validators=[MaxValueValidator(500)]
    )

    # Optional
    school = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    grad_year = models.PositiveSmallIntegerField(null=True, blank=True, 
            validators=[MinValueValidator(2015), MaxValueValidator(2080)],
            db_index=True,
            help_text="4-digit grad year (e.g. 2028)"
    )
    major = models.CharField(max_length=50, blank=True)

    # Socials
    discord = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    #Information
    bio = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="users")
    interests  = models.ManyToManyField(Interest,  blank=True, related_name="users")
    blocked = models.JSONField(null=True,blank=True,default=list)

    # Extra info
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_joined"] # ordered by oldest to newest

    def __str__(self): #how this table is visualized as plain text
        return f"{self.email}"
    
