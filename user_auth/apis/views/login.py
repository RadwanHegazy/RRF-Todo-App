from rrf.views import api_view
from ..serializers import LoginSerializer
from rrf.response import Response

@api_view(['POST'])
def login_view (request) : 
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.tokens, status_code=200)
    return Response(serializer.errors, status_code=400)
    
