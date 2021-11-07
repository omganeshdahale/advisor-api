from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("admin/advisor/", views.AdvisorCreateView.as_view(), name="advisor_create"),
    path("user/register/", views.UserCreateView.as_view(), name="user_create"),
    path(
        "user/<int:user_pk>/advisor/",
        views.AdvisorListView.as_view(),
        name="advisor_list",
    ),
    path(
        "user/<int:user_pk>/advisor/<int:advisor_pk>/",
        views.BookingCreateView.as_view(),
        name="booking_create",
    ),
]
