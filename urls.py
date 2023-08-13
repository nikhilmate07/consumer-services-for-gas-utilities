from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_requests/', views.track_requests, name='request_tracking'),
    path('manage_tickets/', views.manage_tickets, name='manage_tickets'),
]
