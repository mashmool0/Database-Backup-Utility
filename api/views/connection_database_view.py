from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.database_auth_ser import ConnectionParameterSerializer
import psycopg2


class ConnectionView(APIView):

    def post(self, request):
        serializer = ConnectionParameterSerializer(data=request.data)
        if serializer.is_valid():
            database = request.data['name'] or None
            username = request.data['username'] or None
            port = request.data['port'] or None
            host = request.data['host'] or None
            password = request.data['password'] or None

            connection = psycopg2.connect(
                database=database,
                user=username,
                password=password,
                host=host,
                port=port
            )

            cursor = connection.cursor()
            record = cursor.fetchall()
            print("Data from Database:- ", record)

            return Response({'status': "success",
                             "message": "Connected Successfully",
                             "data": serializer.data
                             }, status=status.HTTP_200_OK)

        return Response({"status": "error",
                         "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
