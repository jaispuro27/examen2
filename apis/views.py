from rest_framework import generics
from .serializers import ( PendingSerializer, PendingIDTitleSerializer, PendingIDSerializer, 
PendingUnresolvedSerializer, PendingResolvedSerializer, PendingIDUserIDSerializer,
PendingUnresolvedIDUserIDSerializer,PendingResolvedIDUserIDSerializer,)
from ToDoS.models import Pending

class PendingListView(generics.ListAPIView):
    queryset = Pending.objects.all()
    serializer_class = PendingIDSerializer
    
class PendingListIdsTitlesView(generics.ListAPIView):
    queryset = Pending.objects.all()
    serializer_class = PendingIDTitleSerializer

class PendingListUnresolvedView(generics.ListAPIView):
    queryset = Pending.objects.filter(is_resolved=False)
    serializer_class = PendingUnresolvedSerializer

class PendingListResolvedView(generics.ListAPIView):
    queryset = Pending.objects.filter(is_resolved=True)
    serializer_class = PendingResolvedSerializer

class PendingListIdsUsersView(generics.ListAPIView):
   queryset = Pending.objects.all()
   serializer_class = PendingIDUserIDSerializer

class PendingListResolvedIdsUsersView(generics.ListAPIView):
    queryset = Pending.objects.filter(is_resolved=True)
    serializer_class = PendingResolvedIDUserIDSerializer

class PendingListUnresolvedIdsUsersView(generics.ListAPIView):
    queryset = Pending.objects.filter(is_resolved=False)
    serializer_class = PendingUnresolvedIDUserIDSerializer
    
class PendingCreateView(generics.CreateAPIView):
    queryset = Pending.objects.all()
    serializer_class = PendingSerializer