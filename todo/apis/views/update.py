from rrf.views import api_view
from ..serializers import TodoSerializer, Todo
from rrf.permissions import IsAuthenticated
from rrf.response import Response

@api_view(['PUT'],permissions=[IsAuthenticated])
def update_todo(request, id) : 
    try :
        todo = Todo.objects.get(id=id, user=request.user)
    except Todo.DoesNotExist:
        return Response({
            'message' : 'todo not found'
        }, status_code=404)
    # print(request.data)
    serializer = TodoSerializer(
        data=request.data
    )

    if serializer.is_valid() : 
        serializer.update(todo)
        return Response(serializer.data, status_code=200)
    return Response(serializer.errors, status_code=400)
