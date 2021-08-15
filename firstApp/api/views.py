from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def firstFunction(request):
    return Response({'message': "we received your request"})