# Generated by Django 5.1 on 2024-08-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')], default=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]