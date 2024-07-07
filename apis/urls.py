from django.urls import path
from .views import (
    PendingListView,
    PendingListUnresolvedView,
    PendingListResolvedView,
    PendingCreateView,
    PendingListIdsTitlesView,
    PendingListIdsUsersView,
    PendingListResolvedIdsUsersView,
    PendingListUnresolvedIdsUsersView,
)

urlpatterns = [
    path('list/', PendingListView.as_view(), name='pending-list'),
    path('list/ids-titles/', PendingListIdsTitlesView.as_view(), name='apipending-list-ids-titles'),
    path('list/unresolved/', PendingListUnresolvedView.as_view(), name='apipending-list-unresolved'),
    path('list/resolved/', PendingListResolvedView.as_view(), name='apipending-list-resolved'),
    path('list/ids-users/', PendingListIdsUsersView.as_view(), name='apipending-list-ids-users'),
    path('list/resolved-ids-users/', PendingListResolvedIdsUsersView.as_view(), name='apipending-list-resolved-ids-users'),
    path('list/unresolved-ids-users/', PendingListUnresolvedIdsUsersView.as_view(), name='apipending-list-unresolved-ids-users'),
    path('create/', PendingCreateView.as_view(), name='pending-create'),
]
