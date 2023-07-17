from catalyst.views import PoemInputViewSet, ProfileViewSet, PoemOutputViewSet
from django.urls import path
from catalyst import views

urlpatterns = [
    path('api/profile/<username>', views.ProfileViewSet.as_view()),
    path('api/poem/generate/', views.PoemInputViewSet.as_view()),
    path('api/response/poem/<int:pk>', views.PoemOutputViewSet.as_view()),
    # path('api/visual_art/generate/', views.VisualArtInputViewSet.as_view()),
    # path('api/response/visual_art/<int:pk>',
    #      views.VisualArtOuputViewSet.as_view())
]
# https://api.openai.com/v1/chat/completions
