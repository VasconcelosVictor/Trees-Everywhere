from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PlantedTree
from .serializers import PlantedTreeSerializer

class UserPlantedTreesList(generics.ListAPIView):
    serializer_class = PlantedTreeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlantedTree.objects.filter(user=self.request.user)
