from rest_framework import serializers
from api.models.database_auth import ConnectionParameter


class ConnectionParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionParameter
        exclude = ('id',)
