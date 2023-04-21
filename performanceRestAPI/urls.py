from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.getTickets, name="getTickets"),
    path('ticket', views.createTicket, name="createTicket"),
    path('ticket/<int:ticket_id>', views.ticketOption, name="ticketOption"),
    path('getTicketDatas/<str:artist>', views.getTicketData, name="getTicketData"),
    path('artists', views.getArtists, name="getArtists"),
    path('artist', views.createArtist, name="createArtist"),
    path('artist/<int:artist_id>', views.getOrDeleteArtist, name="getOrDeleteArtist"),
]