"""Models related to allowances reimbursement"""
from django.db import models
from django.db.models import fields


class UserProfile(models.Model):
    """Model for allowance reimbursement declaration"""
    username = fields.CharField(max_length=512, unique=True)
    user_id = fields.IntegerField(editable=False, default=0)
    avatar_url = fields.URLField(null=True, blank=True)
    gravatar_id = fields.IntegerField(editable=False, default=0)
    url = fields.URLField(null=True, blank=True)
    html_url = fields.URLField(null=True, blank=True)
    followers_url = fields.URLField(null=True, blank=True)
    following_url = fields.URLField(null=True, blank=True)
    gists_url = fields.URLField(null=True, blank=True)
    starred_url = fields.URLField(null=True, blank=True)
    subscriptions_url = fields.URLField(null=True, blank=True)
    organizations_url = fields.URLField(null=True, blank=True)
    repos_url = fields.URLField(null=True, blank=True)
    events_url = fields.URLField(null=True, blank=True)
    received_events_url = fields.URLField(null=True, blank=True)
    type = fields.CharField(max_length=127)
    site_admin = models.BooleanField(default=True)
    name = fields.CharField(max_length=127)
    company = fields.CharField(max_length=127)
    blog = fields.URLField(null=True, blank=True)
    location = fields.CharField(max_length=127)
    email = fields.CharField(max_length=127)
    bio = fields.TextField(max_length=512, null=True, blank=True)
    public_repos = fields.IntegerField(editable=False, default=0)
    public_gists = fields.IntegerField(editable=False, default=0)
    followers = fields.IntegerField(editable=False, default=0)
    following = fields.IntegerField(editable=False, default=0)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name = "GitHub User"

    def __unicode__(self):
        return "{}".format(self.user)

