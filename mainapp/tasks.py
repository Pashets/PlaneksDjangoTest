from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder

from mainapp.models import DataSet
from utils_for_tasks import create_csv

logger = get_task_logger(__name__)


@shared_task(bind=True)
def check_download(self, schema_id):
    progress_recorder = ProgressRecorder(self)
    not_ready_datasets = list(DataSet.objects.filter(schema_id=schema_id, state='Processing').all())
    len_not_ready_datasets = len(not_ready_datasets)
    index = 1
    while not_ready_datasets:
        for dataset in not_ready_datasets:
            if dataset.state == 'Ready':
                progress_recorder.set_progress(
                    index,
                    len_not_ready_datasets,
                    description=f'Ready {index} datasets from {len_not_ready_datasets}'
                )
                logger.info(f'{index}/{len_not_ready_datasets}')
                not_ready_datasets.remove(dataset)
            else:
                if create_csv(dataset.id) == 'Done':
                    progress_recorder.set_progress(
                        index,
                        len_not_ready_datasets,
                        description=f'Ready {index} datasets from {len_not_ready_datasets}'
                    )
                    logger.info(f'{index}/{len_not_ready_datasets}')
                    not_ready_datasets.remove(dataset)
            index += 1
    return 'Done'
