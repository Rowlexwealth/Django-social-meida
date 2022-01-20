from rest_framework.decorators import api_view
from rest_framework.response import Response
from pages.models import Room
from .serializers import RoomSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/room',
        'GET /api/room/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, id):
    rooms = Room.objects.get(id=id)
    serializer = RoomSerializer(rooms, many=False)
    return Response(serializer.data)