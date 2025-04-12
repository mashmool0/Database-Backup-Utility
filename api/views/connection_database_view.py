from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.database_auth_ser import ConnectionParameterSerializer
import psycopg2


class ConnectionView(APIView):

    def post(self, request):
        print(request.data)
        serializer = ConnectionParameterSerializer(data=request.data)
        if serializer.is_valid():
            database = request.data.get('database')
            username = request.data.get('username')
            port = request.data.get('port')
            host = request.data.get('host')
            password = request.data.get('password')
            try:
                connection = psycopg2.connect(
                    database=database,
                    user=username,
                    password=password,
                    host=host,
                    port=port
                )
            except psycopg2.Error as e:
                print("Database Connection Error:", e)  # Log the error for debugging
                return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # WRITE QUERY ON DATABASE
            cursor = connection.cursor()
            cursor.execute("select * from categories")
            for rec in cursor:
                print(rec)
            connection.commit()
            cursor.close()

            # Just check connection was successfully or not
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
