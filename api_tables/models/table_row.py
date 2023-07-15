from django.db import models

from api_tables.models.table import get_table_model


class TableRow(models.Model):
    table = models.ForeignKey(get_table_model(), on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
