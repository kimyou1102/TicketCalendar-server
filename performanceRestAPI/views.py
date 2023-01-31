from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TicketSerializer
from .serializer import ArtistSerilalizer
from .models import Ticket
from .models import Artist
from .scrapping import getDatas

# Create your views here.
@api_view(['GET'])
def getTicketData(request, artist):
    information = getDatas(artist)
    mached_artist = Artist.objects.filter(name = artist).values()[0]
    
    for info in information:
        info['artist_id'] = mached_artist['id']

    tikets = Ticket.objects.all()
    serializer = TicketSerializer(tikets, many = True)

    for data in information:
        addTicket(data)

    tikets = Ticket.objects.all()
    serializer = TicketSerializer(tikets, many = True)
    return Response(serializer.data)

def addTicket(scrappingData):
    serializer = TicketSerializer(data=scrappingData)
    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 변환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getTickets(request):
    tikets = Ticket.objects.all()
    serializer = TicketSerializer(tikets, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 변환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getTicketById(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    serializer = TicketSerializer(ticket)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateTicket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    serializer = TicketSerializer(ticket, data=request.data, partial = True)

    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성
    if serializer.is_valid():
        serializer.save() # update
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 변환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTicket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    return Response({'message':'success', 'code': 200})

@api_view(['GET'])
def getArtists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerilalizer(artists, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createArtist(request):
    serializer = ArtistSerilalizer(data=request.data)
    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 변환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getArtistById(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    serializer = ArtistSerilalizer(artist)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteArtist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    artist.delete()
    return Response({'message':'success', 'code': 200})




