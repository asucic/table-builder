from rest_framework import status

from api_tables.models.table import Table
from api_tables.models.table_row import TableRow
from api_tables.tests.views.api.base import AuthenticatedApiTestCase

API_PATH = '/api/table/{table_id}/row'


class ApiTableRowsCreateTest(AuthenticatedApiTestCase):
    def setUp(self):
        super().setUp()

        columns = [
            'column1',
            'column2',
            'column3',
        ]

        self.table = Table.objects.create(name='Test Table', columns=columns)

    def test_create_row_with_correct_data(self):
        data = {
            'column1': 'value1',
            'column2': 'value2',
            'column3': 'value3'
        }

        response = self.client.post(API_PATH.format(table_id=self.table.id), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableRow.objects.count(), 1)
