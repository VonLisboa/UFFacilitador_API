from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cursos, Disciplinas, GradeCurricular, Repositorios, Sistemas, UserDisciplinas


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


class CursosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'


class DisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplinas
        fields = '__all__'


class UserDisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDisciplinas
        fields = '__all__'


class GradeCurricularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GradeCurricular
        fields = '__all__'


class RepositoriosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repositorios
        fields = '__all__'


class SistemasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sistemas
        fields = '__all__'
