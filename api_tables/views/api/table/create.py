from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api_tables.serializers.table import TableSerializer


class ApiTablesCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = TableSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=400)

        serializer.save()
        return Response(serializer.data, status=201)
