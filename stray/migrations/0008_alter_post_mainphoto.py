# Generated by Django 4.2.1 on 2023-05-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stray', '0007_alter_post_mainphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
