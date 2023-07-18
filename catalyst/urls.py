from catalyst.views import AllPromptsArchiveViewSet, MusicInputViewSet, MusicOutputViewSet, MovementInputViewSet, MovementOutputViewSet, WriteInputViewSet, ProfileViewSet, WriteOutputViewSet, VisualArtInputViewSet, VisualArtOutputViewSet
from django.urls import path
from catalyst import views

urlpatterns = [
    path('api/profile/<username>', views.ProfileViewSet.as_view()),
    path('api/write/generate/', views.WriteInputViewSet.as_view()),
    path('api/response/write/<int:pk>', views.WriteOutputViewSet.as_view()),
    path('api/visual_art/generate/', views.VisualArtInputViewSet.as_view()),
    path('api/response/visual_art/<int:pk>',
         views.VisualArtOutputViewSet.as_view()),
    path('api/movement/generate/', views.MovementInputViewSet.as_view()),
    path('api/response/movement/<int:pk>',
         views.MovementOutputViewSet.as_view()),
    path('api/music/generate/', views.MusicInputViewSet.as_view()),
    path('api/response/music/<int:pk>', views.MusicOutputViewSet.as_view()),
    path('api/prompt/archive/',
         views.AllPromptsArchiveViewSet.as_view()),
]
# https://api.openai.com/v1/chat/completions
