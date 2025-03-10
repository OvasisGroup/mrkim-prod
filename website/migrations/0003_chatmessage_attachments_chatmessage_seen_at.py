# Generated by Django 4.2.19 on 2025-03-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='attachments',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='seen_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
