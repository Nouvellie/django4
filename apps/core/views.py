from datetime import datetime, timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from djangonouve.settings import DEBUG
from requirements.info import info
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_426_UPGRADE_REQUIRED,
)
from rest_framework.views import APIView
import re
import time
import traceback


class HomePage(TemplateView):

    template_name = 'core/base.html'


class FirstAPI(APIView):
    
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        result = {
            'version': info['__version__'],
            'author': info['__author__'],
            'created': info['__created__'],
        }
        return Response(result, status=HTTP_200_OK)