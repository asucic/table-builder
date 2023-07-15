from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from api_tables.serializers.table import TableSerializer
from api_tables.models.table import Table
from django.http import JsonResponse


class ApiTablesUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def put(request, table_id):
        try:
            table = Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            return Response({"error": "Table not found."}, status=404)

        serializer = TableSerializer(table, data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()
        return Response(serializer.data, status=200)
