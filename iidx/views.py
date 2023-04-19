from rest_framework.views import APIView
from rest_framework.response import Response

from iidx.models import *


class GetMusicList(APIView):

    def get(self, requests):
        # サイトから曲リストを取ってくる

        #
        print("aa")

        return Response()
