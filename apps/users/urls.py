from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^register/$',
        view=views.UserView.as_view(),
        name='register'
    )
]