from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Human
from .serializers import RegistrationSerializer, ViewsHumanSerializer


class CreateUserAPI(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'User created successfully!'
        return response


class LookUserApi(RetrieveAPIView):
    serializer_class = ViewsHumanSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:

            return Human.objects.get(user=self.request.user)
        except Human.DoesNotExist:

            raise NotFound(detail="Human object not found for this user.")