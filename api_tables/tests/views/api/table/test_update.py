from rest_framework import status

from api_tables.models.table import Table
from api_tables.tests.views.api.base import AuthenticatedApiTestCase

API_PATH = '/api/table/{table_id}'


class ApiTablesUpdateTest(AuthenticatedApiTestCase):
    def test_update_table_columns(self):
        table = Table.objects.create(name="my_table", columns=["column1", "column2", "column3"])
        table_id = table.id
        updated_columns = ["new_column1", "new_column2", "new_column3"]
        data = {
            "name": "my_table",
            "columns": updated_columns
        }

        response = self.client.put(API_PATH.format(table_id=table_id), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        table.refresh_from_db()
        self.assertCountEqual(table.columns, updated_columns)

    def test_update_table_columns_invalid_table(self):
        table_id = 99999  # Invalid table ID
        updated_columns = ["new_column1", "new_column2", "new_column3"]
        data = {
            "name": "my_table",
            "columns": updated_columns
        }

        response = self.client.put(API_PATH.format(table_id=table_id), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_table_columns_invalid_data(self):
        table = Table.objects.create(name="my_table", columns=["column1", "column2", "column3"])
        table_id = table.id
        data = {
            "name": "my_table",
            "columns": ["new_column1", "new_column2"]  # Invalid number of columns
        }

        response = self.client.put(API_PATH.format(table_id=table_id), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        table.refresh_from_db()
        self.assertCountEqual(table.columns, ["column1", "column2", "column3"])
