from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.database_auth_ser import ConnectionParameterSerializer
import psycopg2


class ConnectionView(APIView):

    def post(self, request):
        print(request.data)
        serializer = ConnectionParameterSerializer(data=request.data, many=True)
        if serializer.is_valid():
            print("hello2")
            username = request.data['username'] or None
            port = request.data['port'] or None
            host = request.data['host'] or None
            password = request.data['password'] or None

            connection = psycopg2.connect(
                user=username,
                password=password,
                host=host,
                port=port
            )
            cursor = connection.cursor()
            print(cursor)
            cursor.execute("select * from categories")
            if connection.status == 1:
                return Response({'status': "success",
                                 "message": "Connected Successfully",
                                 "data": serializer.data
                                 }, status=status.HTTP_200_OK)
            return Response({"status": "error",
                             "message": "Doesn't worked please check again!!", },
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "error",
                         "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
