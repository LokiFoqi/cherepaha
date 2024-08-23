from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    date_time_created = models.DateField()

    class Meta:
        db_table = 'books'  # указываем имя таблицы в БД
        managed = False      # Django не будет управлять этой таблицей (миграции не нужны)

    def __str__(self):
        return self.name