from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cursos, Disciplinas, GradeCurricular, Repositorios, Sistemas, UserDisciplinas, Chat


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CursosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'


class DisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplinas
        fields = '__all__'

    def update(self, instance, validated_data):
        # Update the Foo instance
        print(instance.sala)
        instance.sala = validated_data['sala']
        print(instance.sala)
        # instance.save()
        return instance


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


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
