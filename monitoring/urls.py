from django.urls import path
from . import views
app_name = 'monitoring'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings_view/', views.settings_view, name='settings_view'),
    # path('signal/', views.fire_signal, name='signal'),
    path('export_to_excel/', views.export_to_excel, name='export-excel'),
    path('add_data/', views.add_data, name='add-data'),
    path('manual_data_list/', views.data_list, name='manual-data-list'),
    path('get_draft_data/<str:location>', views.get_draft_data, name='get-draft-data'),
    path('scenario_update/<int:scenario_id>/', views.scenario_update, name='scenario-update'),
]