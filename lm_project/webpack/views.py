import os

from django.http import HttpResponse
from django.conf import settings
from urllib.request import urlretrieve

from lm_project.webpack.utils import WebpackTemplateUtil

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


def get_template():
    content = WebpackTemplateUtil.get_latest_template()
    if content:
        return content

    response = urlretrieve(settings.DASHBOARD_TEMPLATE_URL)
    content = open(response[0]).read()
    WebpackTemplateUtil.set_latest_template(content)

    return content


def dashboard(request, path = ''):
    content = get_template()

    return HttpResponse(content)
