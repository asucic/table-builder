from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api_tables.serializers.table_row import TableRowSerializer
from api_tables.models.table import Table


class ApiTableRowsList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, table_id):
        try:
            table = Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            return Response({"error": "Table not found."}, status=404)

        rows = table.get_rows()
        serializer = TableRowSerializer(rows, many=True)
        return Response(serializer.data)
