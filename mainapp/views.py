import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from PlaneksDjangoTest import settings
from .forms import SchemaForm, DataSetForm
from .models import Schema
from .tasks import check_download


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
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        if form.is_valid():
            form.cleaned_data['schema'] = schema
            form.instance.schema = schema
            form.save()
            # task = create_csv.delay(form.instance.id)
            task = check_download.delay(schema_id)
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
    task = check_download.delay(schema_id)
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
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
