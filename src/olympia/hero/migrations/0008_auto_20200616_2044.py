# Generated by Django 2.2.12 on 2020-06-16 20:44

from django.db import migrations, models
import django.db.models.deletion
import olympia.hero.models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0007_auto_20200603_0207_squashed_0010_primaryhero_select_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryhero',
            name='select_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hero.PrimaryHeroImage'),
        )
    ]
