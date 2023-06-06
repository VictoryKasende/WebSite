from datetime import date

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from .models import *
from .forms import CommentaireForm, InscriptionForm, MessageForm, LoginForm


def index(request):
    formations = Formation.objects.all()
    options = Option.objects.all()
    derniers = Article.objects.all().order_by('-id')[:4]
    partenaires = Partenaire.objects.all()
    context = {
        "formations": formations,
        "options": options,
        "derniers": derniers,
        "partenaires": partenaires,
    }
    return render(request, "appSalama/index.html", context)


def option(request, slug: str): 
    option = Option.objects.get(slug=slug)
    cours = Cours.objects.filter(option_id=option.id)
    return render(request, "appSalama/option.html", context={'option': option, 'cours': cours})


def error_404_view(request, exception):
    response = render(request, 'appSalama/404.html')
    response.status_code = 404
    return response


def about(request):
    options = Option.objects.all()
    return render(request, "appSalama/about.html", context={'options':options})

def article(request, slug: str):
    article = Article.objects.get(slug=slug)
    derniers = Article.objects.all().order_by('-id')[:3]
    archives = Archive.objects.all()
    articles = Article.objects.all()
    print("Avant")
    if request.method == 'POST':
        print("In")
        form = CommentaireForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #data = request.POST
            commentaire = Commentaire()
            commentaire.article_id = article.id
            commentaire.email = data['email']
            commentaire.nom = data['nom']
            commentaire.commentaire = data['message']
            commentaire.website = data['website']
            commentaire.date = date.today()
            commentaire.save()
            print(data['nom'])
            print(data['email'])
            print(data['message'])
            print(data['website'])
            print(date.today())
            print(article.id)
            print(data)
            print("Create")

    form = CommentaireForm()
    commentaires = Commentaire.objects.filter(article_id=article.id).order_by('-id')
    if len(commentaires) > 6:
        commentaires = commentaires[:6]


    context = {

        'article': article,
        'articles': articles,
        'commentaires': commentaires,
        'derniers': derniers,
        'archives': archives,
        'form':form,

    }

    return render(request, "appSalama/article.html", context)


def articles(request):
    articles = Article.objects.all()
    derniers = Article.objects.all().order_by('-id')[:3]
    archives = Archive.objects.all()

    context = {
        'articles': articles,
        'derniers': derniers,
        'archives': archives
    }

    return render(request, "appSalama/articles.html", context)

def articles_categorie(request,categorie:str):
    articles = Article.objects.filter(categorie=categorie)
    derniers = Article.objects.all().order_by('-id')[:3]
    archives = Archive.objects.all()

    context = {

        'articles': articles,
        'derniers': derniers,
        'archives': archives,

    }

    return render(request, "appSalama/articles.html", context)

def archive_article(request, mois: str, annee: str):
    articles = Article.objects.filter(date_creation__year=annee)
    derniers = Article.objects.all().order_by('-id')[:3]
    archives = Archive.objects.all()

    context = {

        'articles': articles,
        'derniers': derniers,
        'archives': archives,

    }
    return render(request, "appSalama/articles.html", context)
    

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            inscription = Inscription()
            inscription.user_id = 1
            inscription.nom = data['nom']
            inscription.adresse = data['adresse']
            inscription.date_naissance = data['date_naissance']
            inscription.prenom = data['prenom']
            inscription.post_nom = data['post_nom']
            inscription.motif = data['motif']
            inscription.genre = data['genre']
            inscription.nom_responsable = data['nom_responsable']
            inscription.pourcentage = data['pourcentage']
            inscription.religion = data['religion']
            inscription.save()
    form = InscriptionForm()
    return render(request, "appSalama/inscription.html", context={'form':form})


def realisations(request):
    realisations = Realisation.objects.all().order_by('-id')[:10]
    dernieres_realisations = Realisation.objects.all().order_by('-id')[:4]

    context = {
        'realisations': realisations,
        'dernieres': dernieres_realisations,
    }
    return render(request, "appSalama/realisations.html", context)

def realisation (request, slug: str):
    realisation = Realisation.objects.get(slug=slug)
    dernieres_realisations = Realisation.objects.all().order_by('-id')[:4]

    element_str = realisation.piece
    liste_element = element_str.split(", ")

    context={
        'realisation':realisation, 
        'liste_de_pieces': liste_element,
        'dernieres': dernieres_realisations,
    }

    return render(request, "appSalama/realisation.html", context)


def realisation_option(request, option:str):
    realisations = Realisation.objects.filter(option__nom=option)
    dernieres_realisations = Realisation.objects.all().order_by('-id')[:4]

    context={
        'realisations':realisations, 
        'dernieres': dernieres_realisations,
    }
    
    return render(request, "appSalama/realisations.html", context)
    

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message()
            message.user_id = None
            message.email = data['email']
            message.nom = data['nom']
            message.sujet = data['sujet']
            message.message = data['message']
            message.date = date.today()
            message.save()
    form = MessageForm()
    return render(request, "appSalama/contact.html",context={'form': form})

def infrastructures(request):
    infrastructures = Infrastructure.objects.all()
    return render(request, "appSalama/infrastructures.html", context={'infrastructures':infrastructures})

def infrastructure_categorie (request, categorie: str):
    infrastructure = Infrastructure.objects.get(categorie=categorie)
    return render(request, "appSalama/infrastructure.html", context={'infrastructure':infrastructure})

def connexion(request):
    return redirect("/admin/login/?next=/admin/")
