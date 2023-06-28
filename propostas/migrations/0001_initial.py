# Generated by Django 4.2.2 on 2023-06-28 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CamposProposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='nome')),
                ('tipo', models.CharField(choices=[('text', 'Texto'), ('textarea', 'Texto longo'), ('number', 'Valor'), ('date', 'Data'), ('email', 'E-mail'), ('radio', 'Seleção única')], max_length=20, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='FormProposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(default=False, help_text='Se selecionado este formulário será considerada padrão para visualização do proponente!')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nome da proposta')),
                ('fields', models.ManyToManyField(blank=True, help_text='Selecione os campos para essa proposta!', to='propostas.camposproposta')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(help_text='Escreva uma das opções que deverá ser mostrada ao proponente!', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('False', 'Negada'), ('True', 'Aprovada'), ('Human Approval', 'Avaliação necessária')], max_length=255, null=True)),
                ('documentos', models.JSONField()),
                ('needs_human_approval', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form_proposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propostas.formproposta')),
            ],
        ),
        migrations.AddField(
            model_name='camposproposta',
            name='options',
            field=models.ManyToManyField(blank=True, help_text='Utilizado para campos do tipo Checkbox/Seleção Única', to='propostas.option'),
        ),
    ]
