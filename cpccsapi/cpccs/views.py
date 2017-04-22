from cpccs.models import Sector
from cpccs.models import Ciudad 
from cpccs.models import EstadoCivil 
from cpccs.models import Institucion
from cpccs.models import Nacionalidad
from cpccs.models import NivelEducacion
from cpccs.models import Ocupacion
from cpccs.models import PreDenuncia
from cpccs.models import Provincia
from cpccs.models import Reclamo
from cpccs.models import Region
from cpccs.models import Usuario 

from cpccs.serializers import SectorSerializer 
from cpccs.serializers import CiudadSerializer 
from cpccs.serializers import EstadoCivilSerializer 
from cpccs.serializers import InstitucionSerializer 
from cpccs.serializers import NacionalidadSerializer 
from cpccs.serializers import NivelEducacionSerializer 
from cpccs.serializers import OcupacionSerializer 
from cpccs.serializers import PreDenunciaSerializer 
from cpccs.serializers import ProvinciaSerializer 
from cpccs.serializers import ReclamoSerializer 
from cpccs.serializers import RegionSerializer 
from cpccs.serializers import UsuarioSerializer
 
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

from rest_framework import filters 
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter 
from rest_framework import permissions

from django.core.mail import send_mail

# Create your views here. 
 
class SectorList(generics.ListAPIView): 
    queryset = Sector.objects.all() 
    serializer_class = SectorSerializer 
    name = 'sector-list' 

class CiudadList(generics.ListAPIView): 
    queryset = Ciudad.objects.all() 
    serializer_class = CiudadSerializer 
    name = 'ciudad-list' 
    filter_fields = ('provincia',) 
    search_fields = ('nombre',) 
    ordering_fields = ('nombre',)
	
class EstadoCivilList(generics.ListAPIView): 
    queryset = EstadoCivil.objects.all() 
    serializer_class = EstadoCivilSerializer 
    name = 'estado-civil-list' 

class InstitucionList(generics.ListAPIView): 
    queryset = Institucion.objects.all() 
    serializer_class = InstitucionSerializer 
    name = 'institucion-list' 
    filter_fields = ('nombre',) 
    search_fields = ('nombre',) 
    ordering_fields = ('nombre',) 
	
class NacionalidadList(generics.ListAPIView): 
    queryset = Nacionalidad.objects.all() 
    serializer_class = NacionalidadSerializer 
    name = 'nacionalidad-list' 

class NivelEducacionList(generics.ListAPIView): 
    queryset = NivelEducacion.objects.all() 
    serializer_class = NivelEducacionSerializer 
    name = 'nivel-educacion-list' 

class OcupacionList(generics.ListAPIView): 
    queryset = Ocupacion.objects.all() 
    serializer_class = OcupacionSerializer 
    name = 'ocupacion-list' 

class PreDenunciaList(generics.ListCreateAPIView): 
    queryset = PreDenuncia.objects.all() 
    serializer_class = PreDenunciaSerializer 
    name = 'predenuncia-list' 
    permission_classes = (permissions.IsAuthenticated,)

class ProvinciaList(generics.ListAPIView): 
    queryset = Provincia.objects.all() 
    serializer_class = ProvinciaSerializer 
    name = 'provincia-list' 

class ReclamoList(generics.ListCreateAPIView): 
    queryset = Reclamo.objects.all() 
    serializer_class = ReclamoSerializer 
    name = 'reclamo-list'
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        try:
            descripcion = self.request.data['descripcion']
            tipo = self.request.data['tipo']
            if tipo == '0':
                accion = 'Denuncia'
            elif tipo == '1':
                accion = 'Petición'
        except KeyError:
            descripcion = ''
            accion = 'Petición'
        instance = serializer.save()
        send_mail('<h1>Envio Exitoso</h1> <p>Sr(a) ' + instance.nombresapellidosdenunciante + ' su '+ accion + ' ha sido Enviada Correctamente</p><h3>'+ accion + ': ' + descripcion + '</h3>', 'prueba.envio.formulario@gmail.com', [instance.email],
        fail_silently=False, html_message='<h1>Envio Exitoso</h1> <p>Sr(a) ' + instance.nombresapellidosdenunciante + ' su '+ accion + ' ha sido Enviada Correctamente</p><h3>'+ accion + ': ' + descripcion + '</h3>')

class RegionList(generics.ListAPIView): 
    queryset = Region.objects.all() 
    serializer_class = RegionSerializer 
    name = 'region-list' 
	
class UsuarioList(generics.ListCreateAPIView): 
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioSerializer 
    name = 'usuario-list' 
	
class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'sectores': reverse(SectorList.name, request=request),
            'ciudades': reverse(CiudadList.name, request=request),
            'estados-civiles': reverse(EstadoCivilList.name, request=request),
            'instituciones': reverse(InstitucionList.name, request=request),
            'nacionalidades': reverse(NacionalidadList.name, request=request),
            'niveles-educacion': reverse(NivelEducacionList.name, request=request),
            'ocupaciones': reverse(OcupacionList.name, request=request),
			'predenuncias': reverse(PreDenunciaList.name, request=request),
			'provincias': reverse(ProvinciaList.name, request=request),
			'reclamos': reverse(ReclamoList.name, request=request),
			'regiones': reverse(RegionList.name, request=request),
			'usuarios': reverse(UsuarioList.name, request=request)
            }) 