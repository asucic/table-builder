from rest_framework import serializers
from api_tables.models.table_row import TableRow


class TableRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableRow
        fields = '__all__'
