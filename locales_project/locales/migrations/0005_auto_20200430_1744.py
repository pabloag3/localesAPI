# Generated by Django 3.0.5 on 2020-04-30 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0004_auto_20200430_1727'),
    ]

    operations = [
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
