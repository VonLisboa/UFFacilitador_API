from rest_framework import serializers
from .models import Cursos, Usuarios, Disciplinas, GradeCurricular, Repositorios, Sistemas


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'
        

class DisciplinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplinas
        fields = '__all__'
        

class GradeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeCurricular
        fields = '__all__'
        
class RepositoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repositorios
        fields = '__all__'
        
        
class SistemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistemas
        fields = '__all__'
        
        
# https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa
