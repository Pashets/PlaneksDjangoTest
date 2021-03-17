import os
from time import sleep

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView

from PlaneksDjangoTest import settings
from .forms import SchemaForm, DataSetForm
from .models import Schema, DataSet
from .tasks import create_csv, check_download


def index(request):
    schemas = Schema.objects.all()
    return render(request, 'mainapp/index.html', context={'schemas': schemas})


@login_required
def new_schema(request):
    error = ''
    if request.method == 'POST':
        form = SchemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp')
        else:
            error = 'Форма неверна!'
    form = SchemaForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/new_schema.html', context)


def data_sets_schema(request, schema_id):
    schema = Schema.objects.filter(id=schema_id).first()
    form = DataSetForm()
    error = ''
    task = check_download.delay(schema_id)
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        if form.is_valid():
            form.cleaned_data['schema'] = schema
            form.instance.schema = schema
            form.save()
            create_csv.delay(form.instance.id)
            return render(
                request,
                'mainapp/detail_schema.html',
                {
                    'schema': schema,
                    'data_sets': schema.dataset_set.all(),
                    'form': form,
                    'task_id': task.task_id,
                    'error': error
                }
            )
        else:
            error = 'Форма неверна!'
    return render(
        request,
        'mainapp/detail_schema.html',
        {
            'schema': schema,
            'data_sets': schema.dataset_set.all(),
            'form': form,
            'task_id': task.task_id,
            'error': error
        }
    )


def download(request, file_name):
    a = os.path.abspath(os.curdir)
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # if os.path.exists(file_path):
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404
