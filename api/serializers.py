from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Snippet
from api.models import Cursos, Disciplinas, GradeCurricular, Repositorios, Sistemas


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code',
                  'linenos', 'language', 'style')


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


class DisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplinas
        fields = '__all__'


class DisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplinas
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
