# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github_api_usage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'GitHub User'},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='avatar_url',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='events_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gists_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='html_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='organizations_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='public_gists',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='public_repos',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='received_events_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='repos_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='site_admin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='starred_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='subscriptions_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_id',
        ),
    ]
