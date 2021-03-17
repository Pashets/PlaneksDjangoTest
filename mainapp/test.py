from mainapp.models import Schema, ColumnInSchema

schema_1 = Schema.objects.create(name="Схема 1")  # создали пользователя
m1 = ColumnInSchema.objects.create(schema=schema_1, name="текст сообщения")  # создали пару сообщений
m2 = ColumnInSchema.objects.create(schema=schema_1, name="ещё текст сообщения")
columns = ColumnInSchema.objects.filter(schema=schema_1)
print()