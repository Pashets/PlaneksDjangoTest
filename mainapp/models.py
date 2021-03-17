from django.db import models

# Create your models here.
from django.forms import Select


class Schema(models.Model):
    name = models.CharField(max_length=200, help_text='name of schema')
    column_name_1 = models.CharField(max_length=200, null=True)
    column_type_1 = models.CharField(max_length=100, null=True)
    column_from_1 = models.IntegerField(null=True)
    column_to_1 = models.IntegerField(null=True)
    column_order_1 = models.IntegerField(null=True)
    column_name_2 = models.CharField(max_length=200, null=True)
    column_type_2 = models.CharField(max_length=100, null=True)
    column_from_2 = models.IntegerField(null=True)
    column_to_2 = models.IntegerField(null=True)
    column_order_2 = models.IntegerField(null=True)
    column_name_3 = models.CharField(max_length=200, null=True)
    column_type_3 = models.CharField(max_length=100, null=True)
    column_from_3 = models.IntegerField(null=True)
    column_to_3 = models.IntegerField(null=True)
    column_order_3 = models.IntegerField(null=True)


class DataSet(models.Model):
    number_of_rows = models.IntegerField(null=True)
    state = models.CharField(max_length=30, default='Processing')
    file_name = models.CharField(max_length=100, null=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.schema
