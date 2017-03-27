from rest_framework import serializers 
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
import cpccs.views 
 
class SectorSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Sector
        fields = ( 
            'nombre', 
            'descripcion', 
            'mensaje',
			'control'
			)

class CiudadSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Ciudad
        fields = ( 
            'nombre', 
            'id', 
            'provincia'
			)

class EstadoCivilSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = EstadoCivil
        fields = ( 
            'nombre', 
            'id'
			)

class InstitucionSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Institucion
        fields = ( 
            #'url', 
            #'descripcion',
			#'email',
			'nombre',
			#'representante',
			#'competencia',
			'id',
			'sector'
			)
			
class NacionalidadSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Nacionalidad
        fields = ( 
            'nombre', 
            'id'
			)
		
class NivelEducacionSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = NivelEducacion
        fields = ( 
            'nombre', 
            'descripcion', 
            'id'
			)

class OcupacionSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Ocupacion
        fields = ( 
            'nombre', 
            'descripcion', 
            'id'
			)
			
class PreDenunciaSerializer(serializers.ModelSerializer):  
    tipo = serializers.CharField(source='tipodenuncia')
    genero_denunciante = serializers.CharField(source='generodenunciante')
    descripcion_investigacion = serializers.CharField(source='descripcioninvestigacion')
    genero_denunciado = serializers.CharField(source='generodenunciado')
    funcionario_publico = serializers.CharField(source='funcionariopublico')
    nivel_educacion_denunciante = serializers.PrimaryKeyRelatedField(source='niveleducaciondenunciante', queryset=NivelEducacion.objects.all())
    ocupacion_denunciante = serializers.PrimaryKeyRelatedField(source='ocupaciondenunciante', queryset=Ocupacion.objects.all())
    nacionalidad_denunciante = serializers.PrimaryKeyRelatedField(source='nacionalidaddenunciante', queryset=Nacionalidad.objects.all())
    estado_civil_denunciante = serializers.PrimaryKeyRelatedField(source='estadocivildenunciante', queryset=EstadoCivil.objects.all())
    institucion_implicada = serializers.PrimaryKeyRelatedField(source='institucionimplicada', queryset=Institucion.objects.all())

    class Meta: 
        model = PreDenuncia
        fields = ( 
            'tipo', 
            'genero_denunciante', 
            'descripcion_investigacion',
			'genero_denunciado', 
            'funcionario_publico', 
            'id',
			'nivel_educacion_denunciante', 
            'ocupacion_denunciante', 
            'nacionalidad_denunciante',
			'estado_civil_denunciante', 
            'institucion_implicada'
			)

class ProvinciaSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Provincia
        fields = ( 
            'nombre', 
            'id'
			)			

class ReclamoSerializer(serializers.ModelSerializer):  
    nombres_apellidos_denunciante = serializers.CharField(source='nombresapellidosdenunciante')
    tipo_identificacion = serializers.CharField(source='tipoidentificacion')
    numero_identificacion = serializers.CharField(source='numidenti')
    nombres_apellidos_denunciado = serializers.CharField(source='nombresapellidosdenunciado')
    identidad_reservada = serializers.BooleanField(source='identidadreservada')
    reside_extranjero = serializers.BooleanField(source='resideextrangero')
    ciudad_del_denunciante = serializers.PrimaryKeyRelatedField(source='ciudaddeldenunciante', queryset=Ciudad.objects.all())
    ciudad_del_denunciado = serializers.PrimaryKeyRelatedField(source='ciudaddeldenunciado', queryset=Ciudad.objects.all())
    institucion_implicada = serializers.PrimaryKeyRelatedField(source='institucionimplicada', queryset=Institucion.objects.all())
    provincia_denunciante = serializers.PrimaryKeyRelatedField(source='provinciadenunciante', queryset=Provincia.objects.all())
    provincia_denunciado = serializers.PrimaryKeyRelatedField(source='provinciadenunciado', queryset=Provincia.objects.all())
    
    class Meta: 
        model = Reclamo
        fields = ( 
            'nombres_apellidos_denunciante', 
            'tipo_identificacion', 
            'numero_identificacion',
			'direccion', 
            'email', 
            'nombres_apellidos_denunciado',
			'telefono', 
            'cargo', 
            'comparecer',
			'documentores', 
            'identidad_reservada',
			'reside_extranjero', 
            'id', 
            'ciudad_del_denunciante',
			'ciudad_del_denunciado',
			'institucion_implicada', 
            'provincia_denunciante',
			'provincia_denunciado'
			)
			
class RegionSerializer(serializers.ModelSerializer):  
 
    class Meta: 
        model = Region
        fields = ( 
            'nombre', 
            'descripcion', 
            'id'
			)			
			
class UsuarioSerializer(serializers.ModelSerializer):  
    nombre = serializers.CharField(source='nome')
    telefono = serializers.CharField(source='telefone')

    class Meta: 
        model = Usuario
        fields = ( 
            'id',
			'nombre', 
            'email', 
            'telefono'
			)			