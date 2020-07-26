from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from django.core.mail import send_mail


@api_view(['GET'])
def send(request):
    send_mail('Subject', 'Test message', 'test@django.com', ['laerte.sousaneto@gmail.com'], fail_silently=False)
    return Response(status=HTTP_200_OK)