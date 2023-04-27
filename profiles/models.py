from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static

class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    PHD_YES=1
    PHD_NO=2
    PHD_CHOICES=[
        (PHD_YES, _("Yes")),
        (PHD_NO, _("NO")),
    ]

    DESIGNATION_PROFESSOR = 1
    DESIGNATION_ASSISTANT_PROFESSOR = 2
    DESIGNATION_ASSOCIATE_PROFESSOR = 3
    DESIGNATION_CHOICES=[
        (DESIGNATION_PROFESSOR, _("Professor")),
        (DESIGNATION_ASSISTANT_PROFESSOR, _("Assistant Professor")),
        (DESIGNATION_ASSOCIATE_PROFESSOR, _("Associate Professor"))
    ]

    QUALIFICATIONS_MTECH = "MTECH"
    QUALIFICATIONS_ME = "ME"
    QUALIFICATIONS_MCA = "MCA"
    QUALIFICATIONS_CHOICES=[
        (QUALIFICATIONS_MTECH, _("MTECH")),
        (QUALIFICATIONS_ME, _("ME")),
        (QUALIFICATIONS_MCA, _("MCA"))
    ]
    
    INTERACTION_REPUTED_INSTITUTION = 5
    INTERACTION_INDUSTRY_INSTITUTION = 3
    INTERACTION_CHOICES = [
        (INTERACTION_REPUTED_INSTITUTION, _("Reputed Institution Abroad Or Institution Of Eminence in India Or National Research Laboratories")),
        (INTERACTION_INDUSTRY_INSTITUTION, _("Institution/Industry"))

    ]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    institution = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=32,null=True, blank=True)
    designation = models.PositiveSmallIntegerField(choices=DESIGNATION_CHOICES, null=True, blank=True)
    yearofjoining = models.DateField(null=True, blank=True)
    phd = models.PositiveSmallIntegerField(choices=PHD_CHOICES, null=True, blank=True)
    qualifications = models.CharField(max_length=5,choices=QUALIFICATIONS_CHOICES,null=True, blank=True)

    oneweek = models.BooleanField(default=False)
    program_name01 = models.CharField(max_length=75,null=True, blank=True)
    start_date01 = models.DateField(null=True, blank=True)
    end_date01 = models.DateField(null=True, blank=True)
    location1 = models.CharField(max_length=122,null=True,blank=True)
    twoweek = models.BooleanField(default=False)
    program_name02 = models.CharField(max_length=75,null=True, blank=True)
    start_date02 = models.DateField(null=True, blank=True)
    end_date02 = models.DateField(null=True, blank=True)
    location2 = models.CharField(max_length=122,null=True,blank=True)

    interaction = models.PositiveSmallIntegerField(choices=INTERACTION_CHOICES, null = True, blank = True)
    iiname = models.CharField(max_length=75,null=True, blank=True)
    iidate = models.DateField(null=True, blank=True)
    iiplace = models.CharField(max_length=122,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Publication(models.Model):
    LEVEL_INTERNATIONAL = 5
    LEVEL_NATIONAL = 3 
    LEVEL_STATE = 2
    LEVEL_CHOICES=[
        (LEVEL_INTERNATIONAL,_("International")),
        (LEVEL_STATE,_("State")),
        (LEVEL_NATIONAL,_("National")),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    authors = models.CharField(max_length=200)
    journal_name = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, null=True, blank=True, default=LEVEL_STATE)
    publisher = models.CharField(max_length=200)
    date_published = models.DateField()
    file_upload = models.FileField(upload_to='uploads/')
