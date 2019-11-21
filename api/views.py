from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import Snippet
from api.permissions import IsOwnerOrReadOnly
from api.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from .models import Cursos, Disciplinas, GradeCurricular, Repositorios, Sistemas
from .serializers import CursosSerializer, DisciplinasSerializer, \
    GradeCurricularSerializer, RepositoriosSerializer, SistemasSerializer

class CursosList(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class DisciplinasList(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer

    #def perform_create(self, serializer):
    #    serializer.save(autor=self.request.user)


class GradeCurricularList(viewsets.ModelViewSet):
    queryset = GradeCurricular.objects.all()
    serializer_class = GradeCurricularSerializer


class RepositoriosList(viewsets.ModelViewSet):
    queryset = Repositorios.objects.all()
    serializer_class = RepositoriosSerializer


class SistemasList(viewsets.ModelViewSet):
    queryset = Sistemas.objects.all()
    serializer_class = SistemasSerializer

