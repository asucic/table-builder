from rest_framework import status

from api_tables.models.table import Table
from api_tables.models.table_row import TableRow
from api_tables.tests.views.api.base import AuthenticatedApiTestCase


class GetTableRowsAPITest(AuthenticatedApiTestCase):
    def setUp(self):
        super().setUp()

        self.table = Table.objects.create(name='Test Table', columns=['column1', 'column2'])

        TableRow.objects.create(table=self.table, data={'column1': 'value1', 'column2': 'value2'})
        TableRow.objects.create(table=self.table, data={'column1': 'value3', 'column2': 'value4'})

    def test_get_table_rows(self):
        response = self.client.get(f'/api/table/{self.table.id}/rows')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['data']['column1'], 'value1')
