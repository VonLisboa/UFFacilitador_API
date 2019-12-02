from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cursos', views.CursosList)
router.register(r'disciplinas', views.DisciplinasList, base_name='disciplinas')
router.register(r'grade', views.GradeCurricularList)
router.register(r'repositorios', views.RepositoriosList)
router.register(r'sistemas', views.SistemasList)
router.register(r'users', views.UserViewSet)
router.register(r'userdisciplinas', views.UserDisciplinasList, base_name='userdisciplinas')
router.register(r'chat', views.ChatList, base_name='chat')


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
