from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MeasurementSerializer


class MeasurementBulkCreate(APIView):
    authentication_classes = []
    permission_classes     = []

    def post(self, request):
        if not isinstance(request.data, list):
            return Response({"detail": "Expected a JSON array"}, status=400)

        ser = MeasurementSerializer(data=request.data, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"created": len(ser.data)}, status=status.HTTP_201_CREATED)
