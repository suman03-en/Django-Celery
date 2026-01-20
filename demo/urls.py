from django.urls import path
from .views import RegisterUserView, GenerateReportView

urlpatterns = [
    path("register/", RegisterUserView.as_view()),
    path("generate/",GenerateReportView.as_view()),
]
