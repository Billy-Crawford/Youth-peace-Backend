from django.urls import path

from .views import (
    OSCStatsView,
    UserListView,
    DashboardCourseListView,
    DashboardResourceListView,
    DashboardInitiativeListView,
    DashboardAlertListView,
)

urlpatterns = [

    path(
        "osc/stats/",
        OSCStatsView.as_view()
    ),

    path(
        "osc/users/",
        UserListView.as_view()
    ),

    path(
        "osc/courses/",
        DashboardCourseListView.as_view()
    ),

    path(
        "osc/resources/",
        DashboardResourceListView.as_view()
    ),

    path(
        "osc/initiatives/",
        DashboardInitiativeListView.as_view()
    ),

    path(
        "osc/reports/",
        DashboardAlertListView.as_view()
    ),
]

