from django.urls import path
from .views.api.table import create as api_table_create
from .views.api.table import update as api_table_update
from .views.api.table_row import create as api_table_row_create
from .views.api.table_row import list as api_table_row_list

urlpatterns = [
    path('', api_table_create.ApiTablesCreate.as_view(), name='table-create'),
    path('/<int:table_id>', api_table_update.ApiTablesUpdate.as_view(), name='table-update'),
    path('/<int:table_id>/row', api_table_row_create.ApiTableRowsCreate.as_view(), name='table-row-create'),
    path('/<int:table_id>/rows', api_table_row_list.ApiTableRowsList.as_view(), name='table-row-list'),
]
