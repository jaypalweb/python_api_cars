from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def firstFunction(request):
    print(request.query_params['id'])
    return Response({'message': "we received your request"})