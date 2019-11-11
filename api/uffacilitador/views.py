from rest_framework import generics
from api.uffacilitador.models import Cursos, Usuarios, Disciplinas, GradeCurricular, Repositorios, Sistemas
from api.uffacilitador.serializers import UsuariosSerializer, CursosSerializer, DisciplinasSerializer, GradeCurricularSerializer, RepositoriosSerializer, SistemasSerializer


"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
"""

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    
class CursosList(generics.ListCreateAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer


class DisciplinasList(generics.ListCreateAPIView):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer

    
class GradeCurricularList(generics.ListCreateAPIView):
    queryset = GradeCurricular.objects.all()
    serializer_class = GradeCurricularSerializer


class RepositoriosList(generics.ListCreateAPIView):
    queryset = Repositorios.objects.all()
    serializer_class = RepositoriosSerializer

    
class SistemasList(generics.ListCreateAPIView):
    queryset = Sistemas.objects.all()
    serializer_class = SistemasSerializer
    
