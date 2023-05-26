from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from appAdmin.forms import *
from appSalama.models import *


class IndexListView(TemplateView):
    
    """Compte le nombre d'objets pour chaque modele"""
    template_name = "appAdmin/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbre_article'] = Article.objects.all().count()
        context['nbre_inscription'] = Inscription.objects.all().count()
        context['nbre_partenaire'] = Partenaire.objects.all().count()
        context['nbre_infrastructure'] = Infrastructure.objects.all().count()
        context['nbre_formation'] = Formation.objects.all().count()
        context['nbre_realisation'] = Realisation.objects.all().count()
        context['nbre_option'] = Option.objects.all().count()
        context['nbre_cours'] = Cours.objects.all().count()
        context['nbre_archive'] = Archive.objects.all().count()
        context['nbre_compte'] = CustomUser.objects.all().count()
        
        return context

class ArticleListView(ListView):

    """Afficher les articles, filtre les articles"""
    model = Article
    template_name = "appAdmin/articles.html"
    form_class = ArticleFilter
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        categorie = self.request.GET.get("categorie")
        mois = self.request.GET.get("mois")
        statut = self.request.GET.get("status")

        if nom:
            context['articles'] = context['articles'].filter(titre__icontains=nom)
        
        if categorie:
            context['articles'] = context['articles'].filter(categorie__icontains=categorie)
        """
        if mois:
            context['articles'] = context['articles'].filter(date_creation__month=mois)

        if statut:
            context['articles'] = context['articles'].filter(publié=statut) """

        context['nom_input'] = nom
        context['categorie_input'] = categorie
        context['mois_input'] = mois
        context['statut_input'] = statut
        context["form"] = self.form_class()
        
        return context


class ArticleCreateView(CreateView):

    #Cree un article#
    model = Article
    template_name = "appAdmin/a.html"
    form_class = ArticleForm
    #fields = "__all__"
    success_url = reverse_lazy('appAdmin:article')

    """ def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form) """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class ArticleUpdateView(UpdateView):

    model = Article
    template_name = "appAdmin/a.html"
    form_class = ArticleForm
    success_url = reverse_lazy("appAdmin:article")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context
    

class ArticleDeleteView(DeleteView):

    model = Article
    template_name = "appAdmin/articles.html"
    context_object_name = "article"
    success_url = reverse_lazy("appAdmin:article")

"""
class InscriptionListView(ListView):

    #Afficher les inscriptions, filtre les inscriptions#
    model = Inscription
    template_name = "appAdmin/inscriptions.html"
    form_class = InscriptionFilter
    context_object_name = "inscriptions"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        etablissement = self.request.GET.get('----')
        pourcentage = self.request.GET.get("-----")
        genre = self.request.GET.get("----")

        if nom:
            context['inscriptions'] = context['inscriptions'].filter(titre__icontains=nom)
        
        if etablissement:
            context['inscriptions'] = context['inscriptions'].filter(etablissement__icontains=etablissement)

        if pourcentage:
            context['inscriptions'] = context['inscriptions'].filter(pourcentage=pourcentage)

        if genre:
            context['inscriptions'] = context['inscriptions'].filter(genre__icontains=genre)

        context['nom_input'] = nom
        context['etablissement_input'] = etablissement
        context['pourcentage_input'] = pourcentage
        context['genre_input'] = genre
        
        return context
    

class InscriptionCreateView(CreateView):

    #Cree une inscription, filter les inscriptions#
    model = Inscription
    template_name = "appAdmin/a.html"
    form_class = InscriptionForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:inscription")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context


class InscriptionUpdateView(UpdateView):

    #Modifie une inscription#
    model = Inscription
    template_name = ""
    form_class = InscriptionForm
    success_url = reverse_lazy("appAdmin:inscription")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class InscriptionDeleteView(DeleteView):

    #Supprimer une inscription#
    model = Inscription
    #template_name = ""
    context_object_name = "article"
    success_url = reverse_lazy("appAdmin:inscription")
    

class PartenaireListView(ListView):

    #Afficher les partenaires, filtre les partenaires#
    model = Partenaire
    template_name = "appAdmin/partenaires.html"
    form_class = PartenaireFilter
    context_object_name = "partenaires"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        date = self.request.GET.get('----')

        if nom:
            context['partenaires'] = context['partenaires'].filter(nom__icontains=nom)
        
        if date:
            context['partenaires'] = context['partenaires'].filter(date=date)

        context['nom_input'] = nom
        context['date_input'] = date
        
        return context


class PartenaireCreateView(CreateView):
    #Cree un partenaire, filter les partenaires#
    model = Partenaire
    template_name = "appAdmin/a.html"
    #form_class = 
    fields = "__all__"
    success_url = reverse_lazy("appAdmin:article")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context


class PartenaireUpdateView(UpdateView):

    #Modifie un partenaire#
    model = Partenaire
    template_name = ""
    form_class = PartenaireForm
    success_url = reverse_lazy("appAdmin:partenaire")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class PartenaireDeleteView(DeleteView):

    #Supprimer un partenaire#
    model = Partenaire
    #template_name = ""
    context_object_name = "partenaire"
    success_url = reverse_lazy("appAdmin:partenaire")


class InfrastructureListView(ListView):

    #Afficher les infrastructures, filtre les infrastructures#
    model = Infrastructure
    template_name = "appAdmin/infrastructures.html"
    form_class = InfrastructureFilter
    context_object_name = "infrastructures"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        titre = self.request.GET.get("nom")
        categorie = self.request.GET.get('----')
        date = self.request.GET.get("-----")

        if titre:
            context['infrastructures'] = context['infrastructures'].filter(titre__icontains=titre)
        
        if categorie:
            context['infrastructures'] = context['infrastructures'].filter(categorie__icontains=categorie)

        if date:
            context['infrastructures'] = context['infrastructures'].filter(date=date)

        context['titre_input'] = titre
        context['categorie_input'] = categorie
        context['date_input'] = date

        return context


class InfrastructureCreateView(CreateView):

    #Cree une infrastructure, filter les infrastructures#
    model = Infrastructure
    template_name = "appAdmin/a.html"
    #form_class = InfrastructureForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:article")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class InfrastructureUpdateView(UpdateView):

    #Modifie une infrastructure#
    model = Infrastructure
    template_name = ""
    form_class = FormationForm
    success_url = reverse_lazy("appAdmin:infrastructure")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class InfrastructureDeleteView(DeleteView):

    #Supprimer une infrastructure#
    model = Infrastructure
    #template_name = ""
    context_object_name = "infrastructure"
    success_url = reverse_lazy("appAdmin:infrastructure")


class FormationListView(ListView):

    #Afficher les formations, filtre les formations#
    model = Formation
    template_name = "appAdmin/formations.html"
    form_class = FormationFilter
    context_object_name = "formations"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")

        if nom:
            context['formations'] = context['formations'].filter(nom__icontains=nom)

        context['nom_input'] = nom

        return context


class FormationCreateView(CreateView):

    #Cree une formation, filter les formations#
    model = Formation
    template_name = "appAdmin/a.html"
    form_class = FormationForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:formation")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class FormationUpdateView(UpdateView):

    #Modifie une formation#
    model = Formation
    template_name = ""
    #form_class = InfrastructureForm
    success_url = reverse_lazy("appAdmin:formation")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class FormationDeleteView(DeleteView):

    #Supprimer une formation#
    model = Formation
    #template_name = ""
    context_object_name = "formation"
    success_url = reverse_lazy("appAdmin:formation")


class RealisationListView(ListView):

    #Afficher les realisations, filtre les realisations#
    model = Realisation
    template_name = "appAdmin/realisations.html"
    form_class = RealisationFilter
    context_object_name = "realisations"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        option = self.request.GET.get("")
        date = self.request.Get.get("")

        if nom:
            context['realisations'] = context['realisations'].filter(nom__icontains=nom)
        
        if option:
            context['realisations'] = context['realisations'].filter(option__icontains=option)

        if date:
            context['realisations'] = context['realisations'].filter(date=date)

        context['nom_input'] = nom
        context['option_input'] = option
        context['date_input'] = date

        return context


class RealisationCreateView(CreateView):

    #Cree une realisation, filter les realisations#
    model = Formation
    template_name = "appAdmin/a.html"
    form_class = FormationForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:formation")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class RealisationUpdateView(UpdateView):

    #Modifie une realisation#
    model = Formation
    template_name = ""
    #form_class = InfrastructureForm
    success_url = reverse_lazy("appAdmin:formation")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class RealisationDeleteView(DeleteView):

    #Supprimer une realisation#
    model = Formation
    #template_name = ""
    context_object_name = "formation"
    success_url = reverse_lazy("appAdmin:formation")


class OptionListView(ListView):

    #Afficher les options, filtre les options#
    model = Option
    template_name = "appAdmin/options.html"
    form_class = OptionFilter
    context_object_name = "options"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        categorie = self.request.GET.get("")
        date = self.request.Get.get("")

        if nom:
            context['options'] = context['options'].filter(nom__icontains=nom)
        
        if categorie:
            context['options'] = context['options'].filter(categorie__icontains=categorie)

        if date:
            context['options'] = context['options'].filter(date=date)

        context['nom_input'] = nom
        context['categorie_input'] = categorie
        context['date_input'] = date

        return context


class OptionCreateView(CreateView):

    #Cree une option, filter les options#
    model = Option
    template_name = "appAdmin/a.html"
    form_class = OptionForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:option")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class OptionUpdateView(UpdateView):

    #Modifie une option#
    model = Option
    template_name = ""
    #form_class = InfrastructureForm
    success_url = reverse_lazy("appAdmin:option")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class OptionDeleteView(DeleteView):

    #Supprimer une option#
    model = Option
    #template_name = ""
    context_object_name = "option"
    success_url = reverse_lazy("appAdmin:option")


class CoursListView(ListView):

    #Afficher les cours, filtre les cours#
    model = Cours
    template_name = "appAdmin/cours.html"
    form_class = CoursFilter
    context_object_name = "cours"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        nom = self.request.GET.get("nom")
        section = self.request.GET.get("")
        date = self.request.Get.get("")

        if nom:
            context['cours'] = context['cours'].filter(nom__icontains=nom)
        
        if section:
            context['cours'] = context['cours'].filter(option__nom__icontains=section)

        if date:
            context['cours'] = context['cours'].filter(date=date)

        context['nom_input'] = nom
        context['section_input'] = section
        context['date_input'] = date

        return context


class CoursCreateView(CreateView):

    #Cree un cours, filter les cours#
    model = Option
    template_name = "appAdmin/a.html"
    form_class = CoursForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:cours")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class CoursUpdateView(UpdateView):

    #Modifie un cours#
    model = Cours
    template_name = ""
    #form_class = InfrastructureForm
    success_url = reverse_lazy("appAdmin:cours")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class CoursDeleteView(DeleteView):

    #Supprimer un cours#
    model = Cours
    #template_name = ""
    context_object_name = "cours"
    success_url = reverse_lazy("appAdmin:cours")


class ArchiveListView(ListView):

    #Afficher les archives, filtre les archives#
    model = Archive
    template_name = "appAdmin/archives.html"
    form_class = CoursFilter
    context_object_name = "archives"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        mois = self.request.GET.get("mois")
        annee = self.request.GET.get("")

        if mois:
            context['archives'] = context['archives'].filter(mois=mois)
        
        if annee:
            context['archives'] = context['archives'].filter(annee=annee)

        context['mois_input'] = mois
        context['annee_input'] = annee

        return context


class ArchiveCreateView(CreateView):

    #Cree une archive, filte les archives#
    model = Archive
    template_name = "appAdmin/a.html"
    form_class = ArchiveForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:archive")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class ArchiveUpdateView(UpdateView):

    #Modifie une archive#
    model = Archive
    template_name = ""
    form_class = ArchiveForm
    success_url = reverse_lazy("appAdmin:archive")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class ArchiveDeleteView(DeleteView):

    #Supprimer une archive#
    model = Archive
    #template_name = ""
    context_object_name = "archive"
    success_url = reverse_lazy("appAdmin:archive")


class MessageListView(ListView):

    #Afficher les messages, filtre les messages#
    model = Message
    template_name = "appAdmin/messages.html"
    form_class = MessageFilter
    context_object_name = "messages"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("mois")
        email = self.request.GET.get("")
        date = self.request.GET.get("")

        if nom:
            context['messages'] = context['messages'].filter(nom__icontains=nom)
        
        if email:
            context['messages'] = context['messages'].filter(email__icontains=email)

        if date:
            context['messages'] = context['messages'].filter(date=date)

        context['nom_input'] = nom
        context['email_input'] = email
        context['date_input'] = date

        return context


class MessageCreateView(CreateView):

    #Cree un message, filter les messages#
    model = Message
    template_name = "appAdmin/a.html"
    form_class = MessageForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:message")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class MessageUpdateView(UpdateView):

    #Modifie un message#
    model = Message
    template_name = ""
    form_class = MessageForm
    success_url = reverse_lazy("appAdmin:message")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class MessageDeleteView(DeleteView):

    #Supprimer un message#
    model = Message
    #template_name = ""
    context_object_name = "message"
    success_url = reverse_lazy("appAdmin:message")


class CompteListView(ListView):

    #Afficher les comptes, filtre les comptes#
    model = CustomUser
    template_name = "appAdmin/comptes.html"
    form_class = CompteFilter
    context_object_name = "comptes"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        email = self.request.GET.get("")

        if email:
            context['messages'] = context['messages'].filter(email__icontains=email)

        context['email_input'] = email

        return context


class CompteCreateView(CreateView):

    #Cree un compte, filter les comptes#
    model = CustomUser
    template_name = "appAdmin/a.html"
    form_class = CompteForm
    #fields = "__all__"
    success_url = reverse_lazy("appAdmin:compte")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Ajouter"
        return context
    

class CompteUpdateView(UpdateView):

    #Modifie un compte#
    model = CustomUser
    template_name = ""
    form_class = CompteForm
    success_url = reverse_lazy("appAdmin:compte")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class CompteDeleteView(DeleteView):

    #Supprimer un compte#
    model = CustomUser
    #template_name = ""
    context_object_name = "compte"
    success_url = reverse_lazy("appAdmin:compte")


class CommentaireListView(ListView):

    #Afficher les comptes, filtre les comptes#
    model = Commentaire
    template_name = "appAdmin/commentaires.html"
    form_class = CommentaireFilter
    context_object_name = "commentaires"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("")
        sujet = self.request.GET.get("")
        date = self.request.GET.get("")

        if nom:
            context['commentaires'] = context['commentaires'].filter(nom__icontains=nom)

        if sujet:
            context['commentaires'] = context['commentaires'].filter(sujet__icontains=sujet)
        
        if date:
            context['commentaires'] = context['commentaires'].filter(date=date)

        context['nom_input'] = nom
        context['sujet_input'] = sujet
        context['date_input'] = date

        return context
    

class CommentaireUpdateView(UpdateView):

    #Modifie un compte#
    model = Commentaire
    template_name = ""
    form_class = CommentaireForm
    success_url = reverse_lazy("appAdmin:commentaire")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "Modifier"
        return context


class CommentaireDeleteView(DeleteView):

    #Supprimer un compte#
    model = Commentaire
    #template_name = ""
    context_object_name = "commentaire"
    success_url = reverse_lazy("appAdmin:commenatire")


class ArchiveArticleListView(ListView):

    #Afficher les articles, filtre les articles#
    model = Article
    template_name = "appAdmin/articles.html"
    form_class = ArticleFilter
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        order_croissante = self.request.GET.get('order_by/croissant', 'id')
        order_decroissante = self.request.GET.get('order_by/decroissant', '-id')

        if order_croissante:
            return queryset.order_by(order_croissante)

        if order_decroissante:
            return queryset.order_by(order_decroissante)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        nom = self.request.GET.get("nom")
        categorie = self.request.GET.get('----')
        mois = self.request.GET.get("-----")
        statut = self.request.GET.get("----")

        if nom:
            context['articles'] = context['articles'].filter(titre__icontains=nom)
        
        if categorie:
            context['articles'] = context['articles'].filter(categorie__icontains=categorie)

        if mois:
            context['articles'] = context['articles'].filter(date_creation__month=mois)

        if statut:
            context['articles'] = context['articles'].filter(publié=statut)

        context['nom_input'] = nom
        context['categorie_input'] = categorie
        context['mois_input'] = mois
        context['statut_input'] = statut
        
        return context


class ArchiveArchiveDeleteView(DeleteView):

    #Supprimer un article#
    model = Article
    #template_name = ""
    context_object_name = "article"
    success_url = reverse_lazy("appAdmin:article_archive") """