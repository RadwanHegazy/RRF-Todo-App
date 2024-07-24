from rrf.views import api_view
from ..serializers import TodoSerializer, Todo
from rrf.permissions import IsAuthenticated
from rrf.response import Response

@api_view(['POST'],permissions=[IsAuthenticated])
def create_todo(request) : 
    user = request.user
    data = request.data
    serializer = TodoSerializer(
        data=data,
        context={
            'user' : user
        }
    )
    if serializer.is_valid() :
        serializer.save()
        return Response(status_code=204)
    return Response(serializer.errors,status_code=204)
    