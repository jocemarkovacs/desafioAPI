from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    WorkspacesAPIView, 
    WorkspaceAPIView, 
    VisitsAPIView, 
    VisitAPIView,
    VisitViewSet,
    WorkspaceViewSet)

router = SimpleRouter()
router.register('workspaces', WorkspaceViewSet)
router.register('visits', VisitViewSet)

urlpatterns = [
    path('workspaces/', WorkspacesAPIView.as_view(), name='workspaces'),
    path('workspaces/<int:pk>', WorkspaceAPIView.as_view(), name='workspace'),
    path('workspaces/<int:workspace_pk>/visits/', VisitsAPIView.as_view(), name='workspace_visits'),
    path('workspaces/<int:workspace_pk>/visits/<int:visit_pk>', VisitAPIView.as_view(), name='workspace_avaliacao'),

    path('visits/', VisitsAPIView.as_view(), name='visits'),
    path('visits/<int:visit_pk>', VisitAPIView.as_view(), name='visit'),
]