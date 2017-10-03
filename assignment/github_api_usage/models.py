"""Models related to allowances reimbursement"""
from django.db import models
from django.db.models import fields


class UserProfile(models.Model):
    """Model for allowance reimbursement declaration"""
    username = fields.CharField(max_length=512, unique=True)
    image_url = fields.URLField(null=True, blank=True)
    name = fields.CharField(null=True, max_length=127)
    company = fields.CharField(null=True, max_length=127)
    email = fields.CharField(null=True, max_length=127)

    class Meta:
        verbose_name = "GitHub User"

    def __unicode__(self):
        return "{}".format(self.username)

