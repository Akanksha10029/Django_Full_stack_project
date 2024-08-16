# Generated by Django 5.1 on 2024-08-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_rating_alter_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='video_title',
            field=models.CharField(default='Unknown Title', max_length=500),
        ),
        migrations.AddField(
            model_name='review',
            name='video_url',
            field=models.URLField(default='Unknown URL', max_length=2000),
        ),
    ]
