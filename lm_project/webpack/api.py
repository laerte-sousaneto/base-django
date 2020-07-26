from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from lm_project.webpack.utils import WebpackTemplateUtil


@api_view(['POST'])
def refresh_template(request):
    WebpackTemplateUtil.clear_template()

    return Response(status=HTTP_200_OK)