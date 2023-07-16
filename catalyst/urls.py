from catalyst.views import PoemViewSet, ProfileViewSet, PoemOutputViewSet
from django.urls import path
from catalyst import views

urlpatterns = [
    path('api/profile/<username>', views.ProfileViewSet.as_view()),
    path('api/poem/generate/', views.PoemViewSet.as_view()),
    path('api/response/poem/<int:pk>', views.PoemOutputViewSet.as_view()),
]
# https://api.openai.com/v1/chat/completions
