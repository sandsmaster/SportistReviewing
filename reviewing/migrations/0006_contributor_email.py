# Generated by Django 4.1.7 on 2023-03-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewing', '0005_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
