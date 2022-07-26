from django.urls import path, include
from . import views

urlpatterns = [
    path('mock-quiz/account/', include('django.contrib.auth.urls')),
    path('mock-quiz/account/quiz-<int:QuizNo>/', views.instruction),
    path('mock-quiz/account/quiz-<int:QuizNo>/<int:QuesNo>', views.home),
    path("mock-quiz/account/quiz-<int:QuizNo>/<int:QuesNo>/result", views.result),

    path('mock-quiz/test/', views.test),

    path('mock-quiz/account/login/dashboard/', views.load_dashboard),
]
