from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger import renderers

from .models import Post


class PostView(APIView):
    permission_classes = (IsAuthenticated,)
    enderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    def get(self):
        list_post_list = Post.objects.all().values()
        return Response((list_post_list))
