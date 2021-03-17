import os
import random
from string import ascii_lowercase

from PlaneksDjangoTest import settings
from mainapp.models import DataSet


def create_csv(dataset_id):
    dataset = DataSet.objects.filter(id=dataset_id).first()
    file_path = os.path.join(settings.MEDIA_ROOT, f'{dataset_id}.csv')
    with open(file_path, 'w') as f:
        column_type_1 = dataset.schema.column_type_1
        column_type_2 = dataset.schema.column_type_2
        column_type_3 = dataset.schema.column_type_3
        lines = [f'{dataset.schema.column_name_1},{dataset.schema.column_name_2},{dataset.schema.column_name_3}\n']
        for i in range(dataset.number_of_rows):
            line = ''
            if column_type_1 == 'Full name':
                line += f'{random.choice(["Paul", "Denis", "Olha", "Kate"])} ' \
                        f'{random.choice(["Shevchenko", "Mahno", "Kovalchuk", "Bondar"])},'
            elif column_type_1 == 'Job':
                line += f'{random.choice(["PM", "Developer", "TechLead", "TeamLead"])},'
            elif column_type_1 == 'Email':
                list_with_letters = [ascii_lowercase]
                random.shuffle(list_with_letters)
                line += f'{"".join(list_with_letters)}@{random.choice(["gmail.com", "i.ua", "ukr.net"])},'
            elif column_type_1 == 'Phone number':
                line += f'+{"".join([random.choice([*range(10)]) for _ in range(random.choice([9, 10, 11, 12, 13]))])},'
            elif column_type_1 == 'Integer':
                min_value = min(dataset.schema.column_from_1, dataset.schema.column_to_1)
                max_value = max(dataset.schema.column_from_1, dataset.schema.column_to_1)
                line += f'{random.randrange(min_value, max_value)},'
            if column_type_2 == 'Full name':
                line += f'{random.choice(["Paul", "Denis", "Olha", "Kate"])} ' \
                        f'{random.choice(["Shevchenko", "Mahno", "Kovalchuk", "Bondar"])},'
            elif column_type_2 == 'Job':
                line += f'{random.choice(["PM", "Developer", "TechLead", "TeamLead"])},'
            elif column_type_2 == 'Email':
                list_with_letters = [ascii_lowercase]
                random.shuffle(list_with_letters)
                line += f'{"".join(list_with_letters)}@{random.choice(["gmail.com", "i.ua", "ukr.net"])},'
            elif column_type_2 == 'Phone number':
                line += f'+{"".join([random.choice([*range(10)]) for _ in range(random.choice([9, 10, 11, 12, 13]))])},'
            elif column_type_2 == 'Integer':
                min_value = min(dataset.schema.column_from_2, dataset.schema.column_to_2)
                max_value = max(dataset.schema.column_from_2, dataset.schema.column_to_2)
                line += f'{random.randrange(min_value, max_value)},'
            if column_type_3 == 'Full name':
                line += f'{random.choice(["Paul", "Denis", "Olha", "Kate"])} ' \
                        f'{random.choice(["Shevchenko", "Mahno", "Kovalchuk", "Bondar"])}\n'
            elif column_type_3 == 'Job':
                line += f'{random.choice(["PM", "Developer", "TechLead", "TeamLead"])}\n'
            elif column_type_3 == 'Email':
                list_with_letters = list(ascii_lowercase)
                random.shuffle(list_with_letters)
                line += f'{"".join(list_with_letters)}@{random.choice(["gmail.com", "i.ua", "ukr.net"])}\n'
            elif column_type_3 == 'Phone number':
                line += f'+{"".join([random.choice([*range(10)]) for _ in range(random.choice([9, 10, 11, 12, 13]))])}\n'
            elif column_type_3 == 'Integer':
                min_value = min(dataset.schema.column_from_3, dataset.schema.column_to_3)
                max_value = max(dataset.schema.column_from_3, dataset.schema.column_to_3)
                line += f'{random.randrange(min_value, max_value)}\n'
            lines.append(line)
        f.writelines(lines)
    dataset.state = 'Ready'
    dataset.file_name = f'{dataset_id}.csv'
    dataset.save()
    return 'Done'
