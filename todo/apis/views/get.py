from rrf.views import api_view
from ..serializers import GetListTodoSerializer, Todo
from rrf.permissions import IsAuthenticated
from rrf.response import Response

@api_view(['GET'],permissions=[IsAuthenticated])
def get_todo_list(request) : 
    todos = Todo.objects.filter(user=request.user)
    serializer = GetListTodoSerializer(
        query=todos,
        many=True
    )
    return Response(serializer.data, status_code=200)

@api_view(['GET'],permissions=[IsAuthenticated])
def get_todo(request, id) : 
    try :
        todo = Todo.objects.get(id=id, user=request.user)
    except Todo.DoesNotExist:
        return Response({
            'message' : 'todo not found'
        }, status_code=404)
    
    serializer = GetListTodoSerializer(
        query=todo,
        many=False
    )
    return Response(serializer.data, status_code=200)
