# views.py in your testapp

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def home(request):
    return Response({'status': 200, 'msg': 'This is home'})
