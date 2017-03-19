from rest_framework import serializers 
from cpccs.models import Sector 
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

class UsuarioSerializer(serializers.ModelSerializer):  
    class Meta: 
        model = Usuario
        fields = ( 
            'id',
			'nome', 
            'email', 
            'telefone'
			)			