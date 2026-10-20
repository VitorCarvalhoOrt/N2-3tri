from django.db import migrations


def add_default_platforms(apps, schema_editor):
    Plataforma = apps.get_model('catalogo', 'Plataforma')
    for nome in ('PC', 'PlayStation', 'Xbox', 'Nintendo Switch'):
        Plataforma.objects.get_or_create(nome=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_jogo_descricao_alter_jogo_foto'),
    ]

    operations = [
        migrations.RunPython(add_default_platforms, migrations.RunPython.noop),
    ]
