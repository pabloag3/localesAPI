# Generated by Django 3.0.5 on 2020-04-30 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0002_auto_20200429_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionesEmpresas',
            fields=[
                ('cod_clasificacion_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clasificaciones_empresas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=300)),
                ('longitud', models.CharField(blank=True, max_length=20, null=True)),
                ('latitud', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'empresas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedidasSanitarias',
            fields=[
                ('id_medida_sanitaria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'medidas_sanitarias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpresasMedidas',
            fields=[
                ('id_medida_sanitaria', models.OneToOneField(db_column='id_medida_sanitaria', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='locales.MedidasSanitarias')),
            ],
            options={
                'db_table': 'empresas_medidas',
                'managed': False,
            },
        ),
    ]
