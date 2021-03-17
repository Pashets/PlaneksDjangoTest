from django.forms import ModelForm, TextInput, Select, CharField

from .models import Schema, DataSet


class SchemaForm(ModelForm):
    class Meta:
        model = Schema
        fields = [
            'name',
            'column_name_1',
            'column_type_1',
            'column_from_1',
            'column_to_1',
            'column_order_1',
            'column_name_2',
            'column_type_2',
            'column_from_2',
            'column_to_2',
            'column_order_2',
            'column_name_3',
            'column_type_3',
            'column_from_3',
            'column_to_3',
            'column_order_3'
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название'
                }
            ),
            "column_name_1": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название столбца 1'
                }
            ),
            "column_type_1": Select(
                attrs={
                    'class': 'form-control'
                },
                choices=(
                    ('Full name', 'Full name'),
                    ('Job', 'Job'),
                    ('Email', 'Email'),
                    ('Phone number', 'Phone number'),
                    ('Integer', 'Integer')
                )
            ),
            "column_from_1": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'От',
                }
            ),
            "column_to_1": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'До'
                }
            ),
            "column_order_1": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер'
                }
            ),
            "column_name_2": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название столбца 2'
                }
            ),
            "column_type_2": Select(
                attrs={
                    'class': 'form-control'
                },
                choices=(
                    ('Full name', 'Full name'),
                    ('Job', 'Job'),
                    ('Email', 'Email'),
                    ('Phone number', 'Phone number'),
                    ('Integer', 'Integer')
                )
            ),
            "column_from_2": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'От'
                }
            ),
            "column_to_2": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'До'
                }
            ),
            "column_order_2": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер'
                }
            ),
            "column_name_3": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название столбца 3'
                }
            ),
            "column_type_3": Select(
                attrs={
                    'class': 'form-control'
                },
                choices=(
                    ('Full name', 'Full name'),
                    ('Job', 'Job'),
                    ('Email', 'Email'),
                    ('Phone number', 'Phone number'),
                    ('Integer', 'Integer')
                )
            ),
            "column_from_3": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'От'
                }
            ),
            "column_to_3": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'До'
                }
            ),
            "column_order_3": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер'
                }
            )
        }


class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        fields = [
            'number_of_rows'
        ]
        widgets = {
            "number_of_rows": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите количество рядов'
                }
            )
        }
