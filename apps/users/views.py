from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CustomUserCreationForm


class UserView(APIView):
    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return Response("You are already logged in!", status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'form': CustomUserCreationForm()})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "You can now login!")
            return Response(form)
        return Response(form.errors.as_json, status=status.HTTP_400_BAD_REQUEST)
