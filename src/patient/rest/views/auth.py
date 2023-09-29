from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from ..serializers.auth import PatientAuthSerializer

class PatientAuthListView(CreateAPIView):
    serializer_class = PatientAuthSerializer
    permission_classes = (AllowAny,)