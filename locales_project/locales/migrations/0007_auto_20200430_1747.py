# Generated by Django 3.0.5 on 2020-04-30 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0006_clasificacionesempresas_empresas_empresasmedidas_medidassanitarias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresasmedidas',
            name='id_medida_sanitaria',
        ),
        migrations.DeleteModel(
            name='Empresas',
        ),
        migrations.DeleteModel(
            name='ClasificacionesEmpresas',
        ),
        migrations.DeleteModel(
            name='EmpresasMedidas',
        ),
        migrations.DeleteModel(
            name='MedidasSanitarias',
        ),
    ]
