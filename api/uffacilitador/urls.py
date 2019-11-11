from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^usuarios/$', views.UsuariosList.as_view(), name='usuarios-list'),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view(), name='usuarios-detail'),

    url(r'^cursos/$', views.CursosList.as_view()),
    url(r'^cursos/(?P<pk>[0-9]+)/$', views.CursosDetail.as_view()),
    
    url(r'^disciplinas/$', views.DisciplinasList.as_view()),
    url(r'^disciplinas/(?P<pk>[0-9]+)/$', views.DisciplinasDetail.as_view()),
    
    url(r'^gradecurricular/$', views.GradeCurricularList.as_view()),
    url(r'^gradecurricular/(?P<pk>[0-9]+)/$', views.GradeCurricularDetail.as_view()),
    
    url(r'^repositorios/$', views.RepositoriosList.as_view()),
    url(r'^repositorios/(?P<pk>[0-9]+)/$', views.RepositoriosDetail.as_view()),
    
    url(r'^sistemas/$', views.SistemasList.as_view()),
    url(r'^sistemas/(?P<pk>[0-9]+)/$', views.SistemasDetail.as_view()),

]
