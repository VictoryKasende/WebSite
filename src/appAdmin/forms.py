""" from django import forms
from appSalama.models import *

MOIS = (
    ('mois','Mois...'),
    ('janvier','Janvier'),
    ('fevrier','Février'),
    ('mars','Mars'),
    ('avril', 'Avril'),
    ('mai', 'Mai'),
    ('juin', 'Juin'),
    ('juillet', 'Juillet'),
    ('aout', 'Août'),
    ('septembre', 'Septembre'),
    ('octobre', 'Octobre'),
    ('novembre', 'Novembre'),
    ('decembre', 'Décembre'),
)

GENRES = (
    ('genre','Genre...'),
    ('m','M'),
    ('f','F'),
)

STATUS = (
    ('statut', 'Statut...'),
    ('publier','Publier'),
    ('non_publier','Non Publier'),
)
CATEGORIES = (
    ('categorie', 'Categorie...'),
    ('Construction', 'Construction'),
    ('Commerciale', 'Commerciale'),
    ('Innovation', 'Innovation'),
    ('Structure', 'Structure'),
    ('Securite', 'Securite'),
)

OPTIONS = (
    ('option', 'Option...'),
    ('imprimerie', 'Imprimerie'),
    ('electricite', 'Électricité'),
    ('electronique', 'Électronique'),
    ('mecanique_auto', 'Mécanique Auto'),
    ('mecanique_generale', 'Mécanique Générale'),
    ('mecanique_generale', 'Mécanique Générale'),
    ('machines_outils', 'Machines Outils'),
)

class FormCustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
        ]

        widgets = {
            "email": forms.EmailInput(attrs={'placeholder': "Nom d'utilisateur", 'class': 'form-control'}),
            "password": forms.PasswordInput(attrs={'placeholder': "Mot de passe", 'class': 'form-control'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "titre",
            "paragraphe1",
            "paragraphe2",
            "paragraphe3",
            "paragraphe4",
            "categorie",
            "date_creation",
            "image",
        ]

        widgets = {
            "titre": forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}),
            "paragraphe1": forms.TextInput(attrs={'placeholder': "Paragraphe 1", 'class': 'form-control'}),
            "paragraphe2": forms.TextInput(attrs={'placeholder': "Paragraphe 2", 'class': 'form-control'}),
            "paragraphe3": forms.TextInput(attrs={'placeholder': "Paragraphe 3", 'class': 'form-control'}),
            "paragraphe4": forms.TextInput(attrs={'placeholder': "Paragraphe 4", 'class': 'form-control'}),
            "categorie": forms.TextInput(attrs={'placeholder': "Categorie", 'class': 'form-control'}),
            "date_creation": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "image": forms.FileInput(attrs={'placeholder': "Image", 'class': 'form-control'}),
        }


class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = [
            "image",
            "user",
            "nom",
            "date",
        ]

        widgets = {
            "image": forms.FileInput(attrs={'placeholder': "Image", 'class': 'form-control'}),
            #"nom": forms.TextInput(attrs={'placeholder': "Nom du partenaire", 'class': 'form-control'}),
            #'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = [
            "nom",
            "description",
            'date',
        ]

        widgets = {
            "nom": forms.EmailInput(attrs={'placeholder': "Nom du cours", 'class': 'form-control'}),
            "description": forms.TextInput(attrs={'placeholder': "Description du cours", 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = [
            'nom',
            "description1",
            "image",
        ]

        widgets = {
            'nom':forms.TextInput(),
            "description1":forms.TextInput(),
            "image":forms.TextInput(),
        }

class RealisationForm(forms.ModelForm):
    class Meta:
        model = Realisation
        fields = [
            'option',
            'titre',
            'description',
            'condition',
            'schema',
            'piece',
            'detail',
            'innovateur',
            'date',
            'image',
        ]

        widgets = {
            "email": forms.EmailInput(attrs={'placeholder': "Nom d'utilisateur", 'class': 'form-control'}),
            "password": forms.PasswordInput(attrs={'placeholder': "Mot de passe", 'class': 'form-control'}),
            'option':forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}),
            'description':forms.TextInput(attrs={'placeholder': "Description", 'class': 'form-control'}),
            'condition':forms.TextInput(attrs={'placeholder': "Condition", 'class': 'form-control'}),
            'schema':forms.FileInput(attrs={'placeholder': "Schema", 'class': 'form-control'}),
            'piece':forms.TextInput(attrs={'placeholder': "Piece", 'class': 'form-control'}),
            'detail':forms.TextInput(attrs={'placeholder': "Detail", 'class': 'form-control'}),
            'innovateur': forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}),
            'date': forms.TextInput(attrs={'type': "date", 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'placeholder': "Image", 'class': 'form-control'}),
        }

class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = [
            'titre',
            "date",
            'categorie'
            "image",
        ]

        widgets = {
            'categorie':forms.ChoiceField(choices=CATEGORIES),
            'titre':forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}),
            'date': forms.TextInput(attrs={'type': "date", 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'placeholder': "Image", 'class': 'form-control'}),
        }

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = [
            "mois",
            "annee",
            'date',
        ]

        widgets = {
            "mois": forms.TextInput(attrs={'placeholder': "Mois", 'class': 'form-control'}),
            "annee": forms.TextInput(attrs={'placeholder': "Annee", 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'nom',
            'description1',
            'description2',
            'description3',
            'image',
            'date',
        ]

        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': "Nom de l'option", 'class': 'form-control'}),
            'description1': forms.TextInput(attrs={'placeholder': "Paragraphe 1", 'class': 'form-control'}),
            'description2': forms.TextInput(attrs={'placeholder': "Paragraphe 2", 'class': 'form-control'}),
            'description3': forms.TextInput(attrs={'placeholder': "Paragraphe 3", 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'placeholder': "Image", 'class': 'form-control'}),
        }

class OptionFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de l'option", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
    categorie = forms.ChoiceField(label="", required=True, choices=CATEGORIES)

class CoursFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom du cours", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
    option = forms.ChoiceField(label="", required=True, choices=OPTIONS)

class CommentaireFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de l'internaute", 'class': 'form-control'}))
    sujet = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Sujet", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))

class InfrastructureFilter(forms.Form):
    titre = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Titre", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
    categorie = forms.ChoiceField(label="", required=True, choices=CATEGORIES)

class RealisationFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de la realisation", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
    option = forms.ChoiceField(label="", required=True, choices=OPTIONS)

class CompteFilter(forms.Form):
    email = forms.CharField(label="", required=True,
                           widget=forms.EmailInput(attrs={'placeholder': "Email", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))

class FormationFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de la formation", 'class': 'form-control'}))
    option = forms.ChoiceField(label="", required=True, choices=OPTIONS)

class PartenaireFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'placeholder': "Nom du partenaire", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))

class MessageFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'placeholder': "Nom", 'class': 'form-control'}))
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
    email = forms.CharField(label="", required=True,
                          widget=forms.EmailInput(attrs={'placeholder': "Email", 'class': 'form-control'}))

class ArchiveFilter(forms.Form):
    mois = forms.ChoiceField(label="", required=True, choices=MOIS)
    date = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'type': "date", 'class': 'form-control'}))
class InscriptionFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de l'article", 'class': 'form-control'}))
    nom_etablissement = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Etablissement", 'class': 'form-control'}))
    pourcentage = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Pourcentage", 'class': 'form-control'}))
    genre = forms.ChoiceField(label="", required=True, choices=GENRES)
class ArchiveArticleFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de l'article", 'class': 'form-control'}))
    status = forms.ChoiceField(label="", required=True, choices=STATUS)
    mois = forms.ChoiceField(label="", required=True, choices=MOIS)
    categorie = forms.ChoiceField(label="", required=True, choices=CATEGORIES)

class ArticleFilter(forms.Form):
    nom = forms.CharField(label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': "Nom de l'article", 'class': 'form-control'}))
    status = forms.ChoiceField(label="", required=True, choices=STATUS)
    mois = forms.ChoiceField(label="", required=True, choices=MOIS)
    categorie = forms.ChoiceField(label="", required=True, choices=CATEGORIES)

 """