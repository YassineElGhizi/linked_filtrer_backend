from django.contrib.auth.models import User
from django.db import models
from djangoProject.models import BaseModel
from linkedin.constants import TRACKING_FEEDBACK_CHOICES, COMPANY_SIZE_CHOICES, WORK_MODE_CHOICES


class Company(BaseModel):
    raison_social = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    size = models.CharField(max_length=50, choices=COMPANY_SIZE_CHOICES, null=True, blank=True)


class Search(BaseModel):
    keyword = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    post_time_range = models.PositiveBigIntegerField()
    work_mode = models.CharField(max_length=50, choices=WORK_MODE_CHOICES, null=True, blank=True)


class JobPost(BaseModel):
    url = models.CharField(max_length=600, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    raw_location = models.CharField(max_length=255, null=True, blank=True)
    raw_age = models.IntegerField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    search = models.ForeignKey(Search, on_delete=models.SET_NULL, null=True, blank=True)
    work_mode = models.CharField(max_length=50, choices=WORK_MODE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def view_by_user(self, user: User) -> bool:
        """
        Checks if the JobPost has already been viewed by the given user.
        :param user: The User instance to check for.
        :return: Boolean indicating if a Tracking record exists.
        """
        assert isinstance(user, User)
        return Tracking.objects.filter(job_post=self, user=user).exists()


class Tracking(BaseModel):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255, choices=TRACKING_FEEDBACK_CHOICES,
                                default=TRACKING_FEEDBACK_CHOICES[1][0])

    class Meta:
        unique_together = ('user', 'job_post')
