from catalyst.views import (
    DefinitionOutputViewSet,
    DefinitionInputViewSet,
    WelcomeOutputViewSet,
    WelcomeInputViewSet,
    AllMusicViewSet,
    AllWriteViewSet,
    AllMovementViewSet,
    AllVisualArtViewSet,
    AllMediumsViewSet,
    MusicInputViewSet,
    MusicOutputViewSet,
    MovementInputViewSet,
    MovementOutputViewSet,
    WriteInputViewSet,
    ProfileViewSet,
    WriteOutputViewSet,
    VisualArtInputViewSet,
    VisualArtOutputViewSet,
)
from django.urls import path
from catalyst import views


urlpatterns = [
    # profile
    path('api/profile/<username>', views.ProfileViewSet.as_view()),

    # write
    path('api/write/generate/', views.WriteInputViewSet.as_view()),
    path('api/response/write/<int:pk>', views.WriteOutputViewSet.as_view()),
    path('api/write/', views.AllWriteViewSet.as_view()),

    # visual art
    path('api/visual_art/generate/', views.VisualArtInputViewSet.as_view()),
    path('api/response/visual_art/<int:pk>',
         views.VisualArtOutputViewSet.as_view()),
    path('api/visual_art/', views.AllVisualArtViewSet.as_view()),

    # movement
    path('api/movement/generate/', views.MovementInputViewSet.as_view()),
    path('api/response/movement/<int:pk>',
         views.MovementOutputViewSet.as_view()),
    path('api/movement/', views.AllMovementViewSet.as_view()),

    # music
    path('api/music/generate/', views.MusicInputViewSet.as_view()),
    path('api/response/music/<int:pk>', views.MusicOutputViewSet.as_view()),
    path('api/music/', views.AllMusicViewSet.as_view()),

    # all user prompts/notes
    path('api/folios/',
         views.AllMediumsViewSet.as_view()),

    # welcome
    path('api/welcome/generate/', views.WelcomeInputViewSet.as_view()),
    path('api/welcome/<int:pk>', views.WelcomeOutputViewSet.as_view()),

    # definition
    path('api/definition/generate/', views.DefinitionInputViewSet.as_view()),
    path('api/definition/<int:pk>', views.DefinitionOutputViewSet.as_view()),

]
# https://api.openai.com/v1/chat/completions
