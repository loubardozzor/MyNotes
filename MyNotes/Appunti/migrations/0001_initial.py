# Generated by Django 4.2.4 on 2023-09-01 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Studenti', '0001_initial'),
        ('Materie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto_medio', models.IntegerField()),
                ('Num_scaricamento', models.IntegerField()),
                ('data_caricamento', models.DateTimeField()),
                ('materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Materie.materia')),
                ('studente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Studenti.studente')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('file_pdf', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Scarica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_scaricamento', models.DateTimeField()),
                ('voto_assegnato', models.IntegerField(null=True)),
                ('appunto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Appunti.appunto')),
                ('studente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Studenti.studente')),
            ],
        ),
        migrations.CreateModel(
            name='Recenzione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_recenzione', models.DateTimeField()),
                ('Testo_recenzione', models.CharField(max_length=200)),
                ('appunto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Appunti.appunto')),
                ('studente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Studenti.studente')),
            ],
        ),
        migrations.CreateModel(
            name='Cancella',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cancellazione', models.DateTimeField()),
                ('appunto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Appunti.appunto')),
                ('studente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Studenti.studente')),
            ],
        ),
    ]
