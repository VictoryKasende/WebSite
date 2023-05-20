# Generated by Django 4.2.1 on 2023-05-20 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Adresse mail')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('section1', models.TextField(blank=True, verbose_name='section1')),
                ('section2', models.TextField(blank=True, verbose_name='section2')),
                ('section3', models.TextField(blank=True, verbose_name='section3')),
                ('section4', models.TextField(blank=True, verbose_name='section4')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('publié', models.BooleanField(default=False, verbose_name='Publié')),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('derniere_modification', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='article')),
                ('categorie', models.CharField(choices=[('Construction', 'Construction'), ('Commerciale', 'Commerciale'), ('Innovation', 'Innovation'), ('Structure', 'Structure'), ('Securite', 'Securite')], max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True, verbose_name="Nom de l'option")),
                ('section1', models.TextField(verbose_name='section1')),
                ('section2', models.TextField(verbose_name='section1')),
                ('section3', models.TextField(verbose_name='section1')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='Option', verbose_name='Image')),
                ('date', models.DateField(verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Option',
            },
        ),
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Presentation')),
                ('condition', models.TextField(blank=True, verbose_name='Presentation')),
                ('schema', models.ImageField(blank=True, upload_to='realisation/schema')),
                ('piece', models.TextField(blank=True, max_length=255, verbose_name='Piece')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('innovateur', models.TextField(verbose_name='Innovateur')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='realisation')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appSalama.option', verbose_name='Option')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Realisation',
            },
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partenaire')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('date', models.DateField(verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Partenaire',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('sujet', models.CharField(max_length=255, verbose_name='Sujet')),
                ('message', models.TextField(verbose_name='Message')),
                ('date', models.DateField(verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Message',
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('post_nom', models.CharField(max_length=255, verbose_name='Post nom')),
                ('prenom', models.CharField(max_length=255, verbose_name='Prenom')),
                ('genre', models.CharField(max_length=2, verbose_name='Genre')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('pourcentage', models.IntegerField(verbose_name='Pourcentage')),
                ('adresse', models.CharField(max_length=255, verbose_name='Adresse')),
                ('nom_responsable', models.CharField(max_length=255, verbose_name='Nom de responsable')),
                ('nom_etablissement', models.CharField(max_length=255, verbose_name="Nom de l'etablissement")),
                ('religion', models.CharField(max_length=255, verbose_name='Religion')),
                ('motif', models.TextField(verbose_name='Motif')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Inscription',
            },
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, verbose_name='Titre')),
                ('image', models.ImageField(upload_to='Infrastructure', verbose_name='Image')),
                ('categorie', models.CharField(choices=[('CYCLE SUPERIEUR', 'CYCLE SUPERIEUR'), ('CYCLE INFERIEUR', 'CYCLE INFERIEUR'), ('MECANIQUE GENERALE', 'MECANIQUE GENERALE'), ('MECANIQUE AUTO', 'MECANIQUE AUTO'), ('ELECTRONIQUE', 'ELECTRONIQUE'), ('ELECTRICITE', 'ELECTRICITE'), ('IMPRIMERIE', 'IMPRIMERIE')], max_length=255, verbose_name='Categorie')),
                ('date', models.DateField(verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Infrastructure',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('description1', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='Formation', verbose_name='Image')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Formation',
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField(verbose_name='Date')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSalama.option', verbose_name='Option')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Cours',
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('image_profil', models.ImageField(blank=True, null=True, upload_to='Commentaire', verbose_name='Image')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('website', models.CharField(blank=True, max_length=255, verbose_name='Website')),
                ('commentaire', models.TextField(verbose_name='Commentaire')),
                ('date', models.DateField(verbose_name='Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSalama.article', verbose_name='Article')),
            ],
            options={
                'verbose_name': 'Commentaire',
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(default='1', max_length=255, verbose_name='Mois')),
                ('annee', models.CharField(default='1', max_length=255, verbose_name='Année')),
                ('date', models.DateField(default='1', verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Archive',
            },
        ),
    ]
