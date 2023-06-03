from django.conf.urls.static import static
from django.urls import path, include
from WebSite import settings
from appSalama.views import *

app_name = 'appSalama'

urlpatterns = [
    path('', index, name="home"),
    path('apropos/', about, name="about"),
    path('infrastructure/', infrastructures, name="infrastructure"),
    path('infrastructure/<str:categorie>/', infrastructure_categorie, name="infrastructure"),
    path('realisation/', realisations, name="realisation"),
    path('realisation/<str:slug>/', realisation, name="realisation"),
    path('realisation/filiere/<str:option>/', realisation_option, name="realisation_option"),
    path('inscription/', inscription, name="inscription"),
    path('article/', articles, name="article"),
    path('article/<str:slug>/', article, name="article"),
    path('article/categorie/<str:categorie>/', articles_categorie, name="categorie_article"),
    path('article/archive/<str:mois>/<str:annee>/', archive_article, name="archive_article"),
    path('contact/', contact, name="contact"),
    path("login/", connexion, name="connexion"),
    path('option/<str:slug>/', option, name="option"),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
