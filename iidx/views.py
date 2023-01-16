from rest_framework.views import APIView
from rest_framework.response import Response

from iidx.models import *


class GetMusicList(APIView):

    def get(self, requests):
        b = '嘆きの樹'
        # Musicusic.objects.create(title='嘆きの樹', is_deleted=0)
        Difficulty.objects.create(name='NORMAL', is_deleted=0)
        Difficulty.objects.create(name='HYPER', is_deleted=0)
        Difficulty.objects.create(name='ANOTHER', is_deleted=0)
        Difficulty.objects.create(name='LEGGENDARIA', is_deleted=0)
        return Response(b)
