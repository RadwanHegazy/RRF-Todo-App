from rrf.views import api_view
from ..serializers import Todo
from rrf.permissions import IsAuthenticated
from rrf.response import Response

@api_view(['DELETE'],permissions=[IsAuthenticated])
def delete_todo(request, id) : 
    try :
        todo = Todo.objects.get(id=id, user=request.user)
    except Todo.DoesNotExist:
        return Response({
            'message' : 'todo not found'
        }, status_code=404)
    
    todo.delete()
    return Response(status_code=204)
