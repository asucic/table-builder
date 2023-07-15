from rest_framework import serializers

from api_tables.models.table import Table
from api_tables.serializers.table_row import TableRowSerializer


class TableSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    columns = serializers.ListField(child=serializers.CharField(), required=True)
    rows = TableRowSerializer(many=True, read_only=True)

    def validate_columns(self, columns):
        if self.context['request'].method != 'PUT':
            return columns

        existing_columns_count = len(self.instance.columns) if self.instance else 0

        if len(columns) != existing_columns_count:
            raise serializers.ValidationError("Invalid number of columns. Size must match the existing columns.")

        return columns

    class Meta:
        model = Table
        fields = '__all__'
