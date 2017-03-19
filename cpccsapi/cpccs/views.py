from cpccs.models import Sector
from cpccs.models import Usuario 
from cpccs.serializers import SectorSerializer 
from cpccs.serializers import UsuarioSerializer 
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
# Create your views here. 
 
class SectorList(generics.ListCreateAPIView): 
    queryset = Sector.objects.all() 
    serializer_class = SectorSerializer 
    name = 'sector-list' 
	
class UsuarioList(generics.ListCreateAPIView): 
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioSerializer 
    name = 'usuario-list' 
	
class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'sectors': reverse(Sector.nombre, request=request),
			'usuarios': reverse(Usuario.nombre, request=request)
            }) 