from rest_framework import status

from api_tables.models.table import Table
from api_tables.tests.views.api.base import AuthenticatedApiTestCase

API_PATH = '/api/table'


class ApiTablesCreateTest(AuthenticatedApiTestCase):
    def test_create_table(self):
        data = {
            "name": "my_table",
            "columns": ["column1", "column2", "column3"]
        }

        response = self.client.post(API_PATH, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Table.objects.count(), 1)
        self.assertEqual(Table.objects.first().name, "my_table")
        self.assertCountEqual(Table.objects.first().columns, ["column1", "column2", "column3"])

    def test_create_table_invalid_data(self):
        data = {
            "name": "",  # Invalid name
            "columns": ["column1", "column2", "column3"]
        }

        response = self.client.post(API_PATH, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Table.objects.count(), 0)

    def test_create_table_missing_fields(self):
        data = {
            "name": "my_table"
            # Missing "columns" field
        }

        response = self.client.post(API_PATH, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Table.objects.count(), 0)
