# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-20 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20200820_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
