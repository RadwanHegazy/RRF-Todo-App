from rrf.permissions import IsAuthenticated
from rrf.response import Response
from rrf.views import api_view

@api_view(['GET'], permissions=[IsAuthenticated])
def profile_view (request) : 
    user = request.user
    data = {
        'id' : user.id,
        'username' : user.username,
        'email' : user.email,
    }
    return Response(data, status_code=200)
