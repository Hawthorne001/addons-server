# Generated by Django 4.2.16 on 2024-09-19 09:52

from olympia.constants.promoted import _VERIFIED, _SPONSORED, NOT_PROMOTED
from django.db import migrations


def delete_verified_sponsored_promoted_usage(apps, schema_editor):
    PromotedAddon = apps.get_model('promoted', 'PromotedAddon')
    PromotedApproval = apps.get_model('promoted', 'PromotedApproval')
    PromotedAddon.objects.filter(group_id__in=(_VERIFIED.id, _SPONSORED.id)).update(
        group_id=NOT_PROMOTED.id
    )
    PromotedApproval.objects.filter(group_id__in=(_VERIFIED.id, _SPONSORED.id)).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('promoted', '0020_auto_20221214_1331'),
    ]

    operations = [
        migrations.RunPython(
            delete_verified_sponsored_promoted_usage, migrations.RunPython.noop
        )
    ]
