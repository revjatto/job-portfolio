# Generated by Django 2.2.1 on 2019-06-01 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]