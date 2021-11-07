from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("admin/advisor/", views.AdvisorCreateView.as_view(), name="advisor_create"),
]