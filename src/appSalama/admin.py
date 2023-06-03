from django.contrib import admin
from appSalama.models import *
from django.utils.translation import gettext_lazy, gettext

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "password")

class CoursAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")

class OptionAdmin(admin.ModelAdmin):
    list_display = ("nom", "section1", "section2", "section3", "slug", "image")

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "titre", "section1" , "section2", "section3", "section4", "publié", "date_creation", "derniere_modification", "image", "categorie")
    list_editable = ("publié", )

class FormationAdmin(admin.ModelAdmin):
    list_display = ("nom", "description1", "image")

class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "article",
        "image_profil",
        "email",
        "website",
        "commentaire"
    )

class InscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nom",
        "post_nom",
        "prenom",
        "genre",
        "date_naissance",
        "pourcentage",
        "adresse",
        "nom_responsable",
        "religion",
        "motif",
    )

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "email",
        "sujet",
        "message",
    )


class RealisationAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "description",
        "piece",
        "detail",
        "innovateur",
        "date",
        "slug",
        "option",
        "user",
        "image",
    )


class InfrastructureAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "image",
        "categorie",
        "user",
    )

class ArchiveAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "user",
    )

class PartenaireAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "image",
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(Realisation, RealisationAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Partenaire, PartenaireAdmin)

