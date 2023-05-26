from django.urls import path
from appAdmin.views import *

app_name = "appAdmin"

urlpatterns = [

    path('', IndexListView.as_view(), name="home"),
    
    path('article/', ArticleListView.as_view(), name="article"),
    path('article_create/', ArticleCreateView.as_view(), name="article_create"),
    path('article_update/<str:slug>', ArticleUpdateView.as_view(), name="article_update"),
    path('article_delete/<str:slug>', ArticleDeleteView.as_view(), name="article_delete"),
]
"""

    path('inscription/', InscriptionListView.as_view(), name="inscription"),
    path('inscription_create/', InscriptionCreateView.as_view(), name="inscription_create"),
    path('inscription_update/<int:id>', InscriptionUpdateView.as_view(), name="inscription_update"),
    path('inscription_delete/<int:id>', InscriptionDeleteView.as_view(), name="inscription_delete"),
    path('inscription/ascendant', inscription_order_croissante, name="inscription_ascendant"),
    path('inscription/descendant', inscription_order_decroissante, name="inscription_descendant"),

    path('partenaire/', PartenaireListView.as_view(), name="partenaire"),
    path('partenaire_create/', PartenaireCreateView.as_view(), name="partenaire_create"),
    path('partenaire_update/<int:id>', PartenaireUpdateView.as_view(), name="partenaire_update"),
    path('partenaire_delete/<int:id>', PartenaireDeleteView.as_view(), name="partenaire_delete"),
    path('partenaire/ascendant', partenaire_order_croissante, name="partenaire_ascendant"),
    path('partenaire/descendant', partenaire_order_decroissante, name="partenaire_descendant"),

    path('infrastructure/', InfrastructureListView.as_view(), name="infrastructure"),
    path('infrastructure_create/', InfrastructureCreateView.as_view(), name="infrastructure_create"),
    path('infrastructure_update/<id:id>', InfrastructureUpdateView.as_view(), name="infrastructure_update"),
    path('infrastructure_delete/<int:id>', InfrastructureDeleteView.as_view(), name="infrastructure_delete"),
    path('infrastructure/ascendant', infrastructure_order_croissante, name="infrastructure_ascendant"),
    path('infrastructure/descendant', infrastructure_order_decroissante, name="infrastructure_descendant"),

    path('formation/', FormationListView.as_view(), name="formation"),
    path('formation_create/', FormationCreateView.as_view(), name="formation_create"),
    path('formation_update/<id:id>', FormationUpdateView.as_view(), name="formation_update"),
    path('formation_delete/<int:id>', FormationDeleteView.as_view(), name="formation_delete"),
    path('formation/ascendant', formation_order_croissante, name="formation_ascendant"),
    path('formation/descendant', formation_order_decroissante, name="formation_descendant"),

    path('realisation/', RealisationListView.as_view(), name="realisation"),
    path('realisation_create/', RealisationCreateView.as_view(), name="realisation_create"),
    path('realisation_update/<id:id>', RealisationUpdateView.as_view(), name="realisation_update"),
    path('realisation_delete/<int:id>', RealisationDeleteView.as_view(), name="realisation_delete"),
    path('realisation/ascendant', realisation_order_croissante, name="realisation_ascendant"),
    path('realisation/descendant', realisation_order_decroissante, name="realisation_descendant"),

    path('option/', OptionListView.as_view(), name="option"),
    path('option_create/', OptionCreateView.as_view(), name="option_create"),
    path('option_update/<id:id>', OptionUpdateView.as_view(), name="option_update"),
    path('option_delete/<int:id>', OptionDeleteView.as_view(), name="option_delete"),
    path('option/ascendant', option_order_croissante, name="option_ascendant"),
    path('option/descendant', option_order_decroissante, name="option_descendant"),

    path('cours/', CoursListView.as_view(), name="cours"),
    path('cours_create/', CoursCreateView.as_view(), name="cours_create"),
    path('cours_update/<id:id>', CoursUpdateView.as_view(), name="cours_update"),
    path('cours_delete/<int:id>', CoursDeleteView.as_view(), name="cours_delete"),
    path('cours/ascendant', cours_order_croissante, name="cours_ascendant"),
    path('cours/descendant', cours_order_decroissante, name="cours_descendant"),

    path('archive/', ArchiveListView.as_view(), name="archive"),
    path('archive_create/', ArchiveCreateView.as_view(), name="archive_create"),
    path('archive_update/<id:id>', ArchiveUpdateView.as_view(), name="archive_update"),
    path('archive_delete/<int:id>', ArchiveDeleteView.as_view(), name="archive_delete"),
    path('archive/ascendant', archive_order_croissante, name="archive_ascendant"),
    path('archive/descendant', archive_order_decroissante, name="archive_descendant"),

    path('message/', MessageListView.as_view(), name="message"),
    path('message_create/', MessageCreateView.as_view(), name="message_create"),
    path('message_update/<id:id>', MessageUpdateView.as_view(), name="message_update"),
    path('message_delete/<int:id>', MessageDeleteView.as_view(), name="message_delete"),
    path('message/ascendant', message_order_croissante, name="message_ascendant"),
    path('message/descendant', message_order_decroissante, name="message_descendant"),

    path('compte/', CompteListView.as_view(), name="compte"),
    path('compte_create/', CompteCreateView.as_view(), name="compte_create"),
    path('compte_update/<id:id>', CompteUpdateView.as_view(), name="compte_update"),
    path('compte_delete/<int:id>', CompteDeleteView.as_view(), name="compte_delete"),
    path('compte/ascendant', compte_order_croissante, name="compte_ascendant"),
    path('compte/descendant', compte_order_decroissante, name="compte_descendant"),

    path('commentaire/', CompteListView.as_view(), name="commentaire"),
    path('commentaire_create/', CompteCreateView.as_view(), name="commentaire_create"),
    path('commentaire_update/<id:id>', CompteUpdateView.as_view(), name="commentaire_update"),
    path('commentaire_delete/<int:id>', CompteDeleteView.as_view(), name="commentaire_delete"),
    path('commentaire/ascendant', commentaire_order_croissante, name="commentaire_ascendant"),
    path('commentaire/descendant', commentaire_order_decroissante, name="commentaire_descendant"),

    path('archive_article/', ArchiveArticleListView.as_view(), name="archive_article"),
    path('archive_article_delete/<int:id>', ArchiveArchiveDeleteView.as_view(), name="archive_article_delete"),

]
 """