# Generated by Django 3.1.7 on 2021-03-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210317_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='file_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
