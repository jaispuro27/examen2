from django.urls import path
from .views import (
    PendingListViewIDs,
    PendingListViewIDsTitles,
    PendingListViewUnresolved,
    PendingListViewResolved,
    PendingListViewIDsUsers,
    PendingListViewResolvedIDsUsers,
    PendingListViewUnresolvedIDsUsers,
    apis_index,
    PendingCreateView,
    PendingDetailView 
)

urlpatterns = [
    path('pending-list-ids/', PendingListViewIDs.as_view(), name='pending-list-ids'),
    path('apisindex.html', apis_index, name='apis-index'),
    path('pending-list-ids-titles/', PendingListViewIDsTitles.as_view(), name='pending-list-ids-titles'),
    path('pending-list-unresolved/', PendingListViewUnresolved.as_view(), name='pending-list-unresolved'),
    path('pending-list-resolved/', PendingListViewResolved.as_view(), name='pending-list-resolved'),
    path('pending-list-ids-users/', PendingListViewIDsUsers.as_view(), name='pending-list-ids-users'),
    path('pending-list-resolved-ids-users/', PendingListViewResolvedIDsUsers.as_view(), name='pending-list-resolved-ids-users'),
    path('pending-list-unresolved-ids-users/', PendingListViewUnresolvedIDsUsers.as_view(), name='pending-list-unresolved-ids-users'),
    path('pending-create/', PendingCreateView.as_view(), name='pending-create'),
    
    path('pending-detail/<int:pk>/', PendingDetailView.as_view(), name='pending-detail'),
]
