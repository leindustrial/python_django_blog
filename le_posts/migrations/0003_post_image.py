# Generated by Django 3.2.25 on 2024-04-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('le_posts', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]