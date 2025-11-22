# from django.contrib.auth.models import Group
from .models import User, Skill, Interest, School, Major
from rest_framework import serializers
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError as DjangoValidationError


def ts_to_dt(value):
    """Convert unix timestamp (seconds) -> datetime"""
    if value is None:
        return None
    try:
        # assume seconds
        dt = timezone.datetime.fromtimestamp(int(value), tz=timezone.utc)
        return dt
    except (TypeError, ValueError, OSError):
        raise serializers.ValidationError("Invalid unix timestamp")


def dt_to_ts(dt):
    """Convert datetime -> unix timestamp (seconds)"""
    if not dt:
        return None
    return int(dt.timestamp())

class CustomUserSerializer(serializers.BaseSerializer):
    # INPUT -> PYTHON
    def to_internal_value(self, data):

        # Handle errors
        errors = {}
        url_validator = URLValidator()

        # required fields
        email = data.get('email')
        username = data.get('username')
        if not email:
            errors['email'] = "This field is required"
        if email and email[:-4] != '.edu':
            errors['email'] = "Must be valid school email"
        if not username:
            errors['username'] = "This field is required"

        first = data.get('first_name')
        last = data.get('last_name')


        visibility = data.get('visibility')
        if not visibility:
            errors['visibility'] = "This field is required"
        else:
            visibility = "public" if visibility else "private"

        xp = data.get('xp', 0)
        level = data.get('level', 0)

        def parse_int(name, value, minv=None, maxv=None):
            if value is None:
                return None
            try:
                iv = int(value)
            except (TypeError, ValueError):
                errors[name] = "Must be an integer."
                return None
            if minv is not None and iv < minv:
                errors[name] = f"Must be >= {minv}."
            if maxv is not None and iv > maxv:
                errors[name] = f"Must be <= {maxv}."
            return iv

        xp = parse_int("xp", xp, minv=0)
        level = parse_int("level", level, minv=0, maxv=500)

        school_id = data.get('school') # client gives id
        if school_id is not None:
            try:
                school_id = int(school_id)
                if not School.objects.filter(pk=school_id).exists():
                    errors["school"] = "School does not exist."
            except (TypeError, ValueError):
                errors["school"] = "School must be an integer ID."

        grad_year = data.get('grad_year')
        if grad_year is not None:
            grad_year = parse_int("grad_year", grad_year, minv=2015, maxv=2080)
        major_id = data.get('major') # client gives id
        if major_id is not None:
            try:
                major_id = int(major_id)
                if not Major.objects.filter(pk=major_id).exists():
                    errors["major"] = "Major does not exist."
            except (TypeError, ValueError):
                errors["major"] = "Major must be an integer ID."


        discord = data.get('discord')
        instagram = data.get('instagram')
        github = data.get('github')
        linkedin = data.get('linkedin')

        def validate_url(name, value):
            if not value:
                return value
            try:
                url_validator(value)
            except DjangoValidationError:
                errors[name] = "Enter a valid URL."
            return value

        discord = validate_url("discord", discord)
        instagram = validate_url("instagram", instagram)
        github = validate_url("github", github)
        linkedin = validate_url("linkedin", linkedin)

        bio = data.get('bio', "")

        # client gives lists of IDs (M2M)
        skills = data.get('skills', [])
        if skills is None:
            skills = []
        if not isinstance(skills, list):
            errors["skills"] = "Must be a list of IDs."
        else:
            # ensure they exist
            bad_ids = [sid for sid in skills if not Skill.objects.filter(pk=sid).exists()]
            if bad_ids:
                errors["skills"] = f"Some skills do not exist: {bad_ids}"

        interests = data.get('interests', [])
        if interests is None:
            interests = []
        if not isinstance(interests, list):
            errors["interests"] = "Must be a list of IDs."
        else:
            bad_ids = [iid for iid in interests if not Interest.objects.filter(pk=iid).exists()]
            if bad_ids:
                errors["interests"] = f"Some interests do not exist: {bad_ids}"


        blocked = data.get('blocked', []) # client gives list
        if blocked is None:
            blocked = []
        if not isinstance(blocked, list):
            errors["blocked"] = "Must be a list"

        if errors:
            raise serializers.ValidationError(errors)

        # Resolve FKs in create/update
        # IDs will be getting passed here for the M2M and O2M fields
        return {
            "email": email,
            "username": username,
            "first_name": first,
            "last_name": last,
            "visibility": visibility,
            "xp": xp,
            "level": level,
            "school_id": school_id,
            "grad_year": grad_year,
            "major_id": major_id,
            "discord": discord,
            "instagram": instagram,
            "github": github,
            "linkedin": linkedin,
            "bio": bio,
            "skills": skills,
            "interests": interests,
            "blocked": blocked,
        }

    # PYTHON -> OUTPUT
    def to_representation(self, instance: User):
        # no need for check b/c coming from db 
        return {
            "id": str(instance.id),
            "email": instance.email,
            "username": instance.username,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "visibility": instance.visibility,
            "xp": instance.xp,
            "level": instance.level,
            "school": instance.school.id if instance.school else None,
            "school_name": instance.school.name if instance.school else None,
            "grad_year": instance.grad_year,
            "major": instance.major.id if instance.major else None,
            "major_name": instance.major.name if instance.major else None,
            "discord": instance.discord,
            "instagram": instance.instagram,
            "github": instance.github,
            "linkedin": instance.linkedin,
            "bio": instance.bio,
            "skills": [s.id for s in instance.skills.all()],
            "skill_names": [s.name for s in instance.skills.all()],
            "interests": [i.id for i in instance.interests.all()],
            "interest_names": [i.name for i in instance.interests.all()],
            "blocked": instance.blocked,
            "date_joined": dt_to_ts(instance.date_joined),
        }

    # called by serializer.save when instance is None
    def create(self, validated_data):

        # get m2m + fk IDs first
        skill_ids = validated_data.pop("skills", [])
        interest_ids = validated_data.pop("interests", [])
        school_id = validated_data.pop("school_id", None)
        major_id = validated_data.pop("major_id", None)

        # set FKs if provided
        if school_id:
            validated_data["school"] = School.objects.get(pk=school_id)
        if major_id:
            validated_data["major"] = Major.objects.get(pk=major_id)

        user = User.objects.create(**validated_data)

        if skill_ids:
            user.skills.set(Skill.objects.filter(id__in=skill_ids))
        if interest_ids:
            user.interests.set(Interest.objects.filter(id__in=interest_ids))

        return user

    # called by serializer.save when instance exists
    def update(self, instance: User, validated_data):
        skill_ids = validated_data.pop("skills", None)
        interest_ids = validated_data.pop("interests", None)
        school_id = validated_data.pop("school_id", None)
        major_id = validated_data.pop("major_id", None)

        # simple fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # fks
        if school_id is not None:
            instance.school = School.objects.get(pk=school_id) if school_id else None
        if major_id is not None:
            instance.major = Major.objects.get(pk=major_id) if major_id else None

        instance.save()

        # m2m
        if skill_ids is not None:
            instance.skills.set(Skill.objects.filter(id__in=skill_ids))
        if interest_ids is not None:
            instance.interests.set(Interest.objects.filter(id__in=interest_ids))

        return instance
