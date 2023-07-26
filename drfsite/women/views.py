from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LeatherClothes, Category
from .pagination import LeatherAPIListPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import LeatherSerializer


# Create your views here.
# class LeatherViewSet(viewsets.ModelViewSet):
#     # queryset = LeatherClothes.objects.all()
#     serializer_class = LeatherSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return LeatherClothes.objects.all()[:3]
#
#         return LeatherClothes.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})
#
#

class LeatherAPIView(generics.ListAPIView):
    queryset = LeatherClothes.objects.all()
    serializer_class = LeatherSerializer


class LeatherAPIList(generics.ListCreateAPIView):
    queryset = LeatherClothes.objects.all()
    serializer_class = LeatherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = LeatherAPIListPagination


class LeatherAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = LeatherClothes.objects.all()
    serializer_class = LeatherSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class LeatherAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = LeatherClothes.objects.all()
    serializer_class = LeatherSerializer
    permission_classes = (IsAdminOrReadOnly, )

