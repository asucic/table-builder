from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api_tables.serializers.table_row import TableRowSerializer
from api_tables.models.table import Table


class ApiTableRowsCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request, table_id):
        try:
            table = Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            return Response({"error": "Table not found."}, status=404)

        data = request.data.copy()
        data['table'] = table.id

        serializer = TableRowSerializer(data=data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=400)

        serializer.save(table=table)
        return Response(serializer.data, status=201)
