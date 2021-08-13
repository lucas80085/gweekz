from django.urls import path, include

from .views import (
    user_redirect_view,
    user_detail_view,
)

app_name = "accounts"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]

