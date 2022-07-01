from dataclasses import dataclass
from rest_framework import serializers
from .models import Workspaces, Visits


class VisitsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Visits
        fields = (
            'id',
            'dataField',
            'yearField',
            'monthField',
            'dayOfMonth',
            'dayOfWeek',
            'workspace'
        )
        

class WorkspacesSerializer(serializers.ModelSerializer):
    
    visits = VisitsSerializer(many=True, read_only=True)
    

    class Meta:
        model = Workspaces
        fields = (
            'id',
            'name',
            'kind',
            'description',
            'visits'
        )
        


        