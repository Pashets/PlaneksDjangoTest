# Generated by Django 3.1.7 on 2021-03-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210317_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='state',
            field=models.CharField(default='Created', max_length=30),
        ),
    ]
