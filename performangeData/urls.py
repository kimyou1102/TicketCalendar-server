"""performangeData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from performanceRestAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tickets', views.getTickets, name="getTickets"),
    path('api/ticket', views.createTicket, name="createTicket"),
    path('api/ticket/<int:ticket_id>', views.ticketOption, name="ticketOption"),
    path('getTicketDatas/<str:artist>', views.getTicketData, name="getTicketData"),
    path('api/artists', views.getArtists, name="getArtists"),
    path('api/artist', views.createArtist, name="createArtist"),
    path('api/artist/<int:artist_id>', views.getOrDeleteArtist, name="getOrDeleteArtist"),
]
