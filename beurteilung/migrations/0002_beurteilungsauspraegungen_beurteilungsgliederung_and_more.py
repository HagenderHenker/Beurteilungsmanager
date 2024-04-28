# Generated by Django 5.0.4 on 2024-04-21 19:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beurteilung', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beurteilungsauspraegungen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilungsausprägung', models.CharField(max_length=50)),
                ('punktwert', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Beurteilungsgliederung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gliederung', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Beurteilungstemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilungstemplate_bezeichnung', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Beurteilungen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilung_bez', models.CharField(max_length=255)),
                ('beurteilung_erl', models.CharField(max_length=255)),
                ('frist_erstbeurteilung', models.DateField()),
                ('frist_zweitbeurteilung', models.DateField()),
                ('beurteilter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('erstbeurteiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='erstbeurteiler', to=settings.AUTH_USER_MODEL)),
                ('zweitbeurteiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zweitbeurteiler', to=settings.AUTH_USER_MODEL)),
                ('beurteilungstemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungstemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Beurteilungsmerkmale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilungsmerkmal', models.CharField(max_length=50)),
                ('beurteilungsauspraegungen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungsauspraegungen')),
                ('untergruppe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungsgliederung')),
                ('beurteilungstemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungstemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Beurteilung_Beurteilungsmerkmale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungen')),
                ('be_auspraegung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungsauspraegungen')),
                ('be_merkmal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungsmerkmale')),
            ],
        ),
        migrations.AddField(
            model_name='beurteilungsgliederung',
            name='beurteilungstemplate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungstemplate'),
        ),
        migrations.CreateModel(
            name='Beurteilungsadressaten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beurteilungstemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beurteilung.beurteilungstemplate')),
            ],
        ),
    ]