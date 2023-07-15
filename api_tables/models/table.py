from django.db import models
from django.contrib.auth.models import User

from django.apps import apps


def get_table_model():
    return apps.get_model('api_tables', 'Table')


def get_table_row_model():
    return apps.get_model('api_tables', 'TableRow')


class Table(models.Model):
    name = models.CharField(max_length=255)
    columns = models.JSONField(default=list)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def add_row(self, row_data):
        table_row_model = get_table_row_model()
        row = table_row_model(table=self, data=row_data)
        row.save()

    def get_rows(self):
        return get_table_row_model().objects.filter(table=self)
