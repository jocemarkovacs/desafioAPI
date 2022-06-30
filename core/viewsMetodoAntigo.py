from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Workspaces, Visits
from .serializers import WorkspacesSerializer, VisitsSerializer

class WorkspacesAPIView(APIView):
    """
    API Workspace
    """
    def get(self, resquest):
        workspace = Workspaces.objects.all()
        serializer = WorkspacesSerializer(workspace, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkspacesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VisitsAPIView(APIView):
    """
    API Visits
    """
    def get(self, resquest):
        visits = Visits.objects.all()
        serializer = VisitsSerializer(visits, many=True)
        return Response(serializer.data)
   