from rrf.views import api_view
from ..serializers import RegisterSerialier
from rrf.response import Response

@api_view(['POST'])
def register_view (request) : 
    serializer = RegisterSerialier(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.tokens, status_code=200)
    return Response(serializer.errors, status_code=400)
    
