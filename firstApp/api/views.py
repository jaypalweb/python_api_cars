from django.http import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    # print(request.query_params['id'])
    return Response({'message': "we received your request"})