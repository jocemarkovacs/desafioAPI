from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Visits, Workspaces
from core.serializers import VisitsSerializer, WorkspacesSerializer

"""
API V1
"""

class WorkspacesAPIView(generics.ListCreateAPIView):
    queryset = Workspaces.objects.all()
    serializer_class = WorkspacesSerializer

class WorkspaceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workspaces.objects.all()
    serializer_class = WorkspacesSerializer

class VisitsAPIView(generics.ListCreateAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer

    def get_queryset(self):
        if self.kwargs.get('workspace_pk'):
            return self.queryset.filter(workspace_id=self.kwargs.get('workspace_pk'))
        return self.queryset.all()
    

class VisitAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer

    def get_object(self):
        if self.kwargs.get('workspace_pk'):
            return get_object_or_404(
                self.get_queryset(),
                workspace_id=self.kwargs.get('workspace_pk'),
                pk=self.kwargs.get('visit_pk')
            )
        #caso contrario retorna a avaliacao
        return (get_object_or_404(
                self.get_queryset(), 
                pk=self.kwargs.get('visit_pk')
                )
        )

"""
API V2
"""
class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspaces.objects.all()
    serializer_class = WorkspacesSerializer
    
    @action(detail=True, methods=['get'])#detail=True para criar a rota
    def visits(self, request, pk=None):

        workspace = self.get_object()
        serializer = VisitsSerializer(workspace.workspace_id.all(), many=True)
        return Response(serializer.data)


class VisitViewSet(viewsets.ModelViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visits = None
        self.queryset = None

    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer

    @action(detail=True, methods=['get'])
    def get_queryset(self):
        """
        Retorna todas as visitas segundo pesquisa via QueryString
        Ex URI: /visits/?data=2022-06-27
        """
        queryset = Visits.objects.all()

        data = self.request.query_params.get('data')
        depth = self.request.query_params.get('depth')
        
        if data is not None:
            queryset = queryset.filter(dataField=data)

        app = queryset.filter(workspace_id=1).count()
        site = queryset.filter(workspace_id=2).count()

        self.visits = {	
            "visits":{
                "app": {app}, "site": {site}
            }
        }

        # print(f'VISITS: {self.visits}')            
        
        if depth is not None:
            if depth == '1':
                VisitsSerializer.Meta.depth = 1
            if depth == '0':
                VisitsSerializer.Meta.depth = 0

        
        for object in queryset:
            object1 = object.__dict__
            object1['visits']=self.visits
            
            print(object1)
        
        
        
        
        return queryset

    
            

