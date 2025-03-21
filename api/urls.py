from django.urls import path
from api.views.connection_database_view import ConnectionView

app_name = 'api'
urlpatterns = [
    path('', ConnectionView.as_view(), name="connection")
]
