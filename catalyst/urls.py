from catalyst.views import DefinitionOutputViewSet, DefinitionInputViewSet, WelcomeOutputViewSet, WelcomeInputViewSet, NoteRetrieveUpdateDestroyViewSet, NoteArchiveViewSet, AllMusicPromptViewSet, AllWritePromptViewSet, AllMovementPromptViewSet, AllVisualArtPromptViewSet, AllPromptsArchiveViewSet, MusicInputViewSet, MusicOutputViewSet, MovementInputViewSet, MovementOutputViewSet, WriteInputViewSet, ProfileViewSet, WriteOutputViewSet, VisualArtInputViewSet, VisualArtOutputViewSet
from django.urls import path
from catalyst import views


urlpatterns = [
    # profile
    path('api/profile/<username>', views.ProfileViewSet.as_view()),

    # write
    path('api/write/generate/', views.WriteInputViewSet.as_view()),
    path('api/response/write/<int:pk>', views.WriteOutputViewSet.as_view()),
    path('api/write/prompts/', views.AllWritePromptViewSet.as_view()),

    # visual art
    path('api/visual_art/generate/', views.VisualArtInputViewSet.as_view()),
    path('api/response/visual_art/<int:pk>',
         views.VisualArtOutputViewSet.as_view()),
    path('api/visual_art/prompts/', views.AllVisualArtPromptViewSet.as_view()),

    # movement
    path('api/movement/generate/', views.MovementInputViewSet.as_view()),
    path('api/response/movement/<int:pk>',
         views.MovementOutputViewSet.as_view()),
    path('api/movement/prompts/', views.AllMovementPromptViewSet.as_view()),

    # music
    path('api/music/generate/', views.MusicInputViewSet.as_view()),
    path('api/response/music/<int:pk>', views.MusicOutputViewSet.as_view()),
    path('api/music/prompts/', views.AllMusicPromptViewSet.as_view()),

    # note
    path('api/note/create/', views.NoteCreateViewSet.as_view()),
    path('api/note/<int:pk>', views.NoteRetrieveUpdateDestroyViewSet.as_view()),
    path('api/note/archive/', views.NoteArchiveViewSet.as_view()),

    # all user prompts
    path('api/prompt/archive/',
         views.AllPromptsArchiveViewSet.as_view()),

    # welcome
    path('api/welcome/generate/', views.WelcomeInputViewSet.as_view()),
    path('api/welcome/<int:pk>', views.WelcomeOutputViewSet.as_view()),

    # definition
    path('api/definition/generate/', views.DefinitionInputViewSet.as_view()),
    path('api/definition/<int:pk>', views.DefinitionOutputViewSet.as_view()),

]
# https://api.openai.com/v1/chat/completions
