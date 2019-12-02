from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404

from api.serializers import UserSerializer, UserDisciplinasSerializer
from api.models import Cursos, Disciplinas, GradeCurricular, Repositorios, Sistemas, UserDisciplinas, Chat
from api.serializers import CursosSerializer, DisciplinasSerializer, \
    GradeCurricularSerializer, RepositoriosSerializer, SistemasSerializer, ChatSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CursosList(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class DisciplinasList(viewsets.ModelViewSet):
    serializer_class = DisciplinasSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Disciplinas.objects.filter(pk=self.kwargs['pk'])

        user_id = self.request.query_params.get('user_id')
        is_admin = self.request.query_params.get('is_admin')

        if is_admin == '1':
            queryset = Disciplinas.objects.all()
        else:
            queryset = Disciplinas.objects.all().filter(Q(status=1) | Q(autor=user_id))
        return queryset

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Disciplinas.objects.get(id=pk)


class UserDisciplinasList(viewsets.ModelViewSet):
    serializer_class = UserDisciplinasSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return UserDisciplinas.objects.get(id=pk)

    def get_queryset(self):
        disciplina = self.request.query_params.get('disciplina')
        user_id = self.request.query_params.get('user_id')
        first = self.request.query_params.get('first')
        if disciplina:
            queryset = UserDisciplinas.objects.all().filter(user_id=user_id, disciplina=disciplina)
        else:
            queryset = UserDisciplinas.objects.all().filter(user_id=user_id)
        if first != '1':
            return queryset
        items, item_ids = [], []
        for item in queryset:
            if item.disciplina not in item_ids:
                items.append(item)
                item_ids.append(item.disciplina)

        return items

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class GradeCurricularList(viewsets.ModelViewSet):
    queryset = GradeCurricular.objects.all()
    serializer_class = GradeCurricularSerializer


class RepositoriosList(viewsets.ModelViewSet):
    queryset = Repositorios.objects.all()
    serializer_class = RepositoriosSerializer


class SistemasList(viewsets.ModelViewSet):
    queryset = Sistemas.objects.all()
    serializer_class = SistemasSerializer


class ChatList(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Disciplinas.objects.filter(pk=self.kwargs['pk'])

        offset = self.request.query_params.get('offset')
        if offset:
            queryset = Chat.objects.all().order_by('id')[int(offset):]
        else:
            queryset = Chat.objects.all()

        return queryset