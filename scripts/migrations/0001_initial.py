# Generated by Django 2.2.2 on 2019-06-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True)),
                ('titulo', models.CharField(blank=True, max_length=250, null=True)),
                ('texto', models.TextField()),
            ],
        ),
    ]