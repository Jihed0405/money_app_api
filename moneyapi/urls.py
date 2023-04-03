from django.urls import path

from . import views

urlpatterns = [
  path('money/', views.MoneyApiView.as_view()),
  path('money/<int:id>/', views.MoneyApiView.as_view()),
]