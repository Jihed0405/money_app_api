from django.urls import path

from . import views

urlpatterns = [
  path('api/v2/money/', views.MoneyApiView.as_view()),
  path('api/v2/money/<int:id>/', views.MoneyApiView.as_view()),
]