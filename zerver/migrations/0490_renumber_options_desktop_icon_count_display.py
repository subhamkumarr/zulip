# Generated by Django 4.2.7 on 2023-11-17 04:55

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

OLD_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION = 2
NEW_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION = 3
OLD_DESKTOP_ICON_COUNT_DISPLAY_NONE = 3
NEW_DESKTOP_ICON_COUNT_DISPLAY_NONE = 4


def renumber_options(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    # We added a new option 'DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION_FOLLOWED_TOPIC'
    # for 'desktop_icon_count_display' setting. It has the value 2.
    # The following options are renumbered:
    # * 'DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION' from 2 to 3
    # * 'DESKTOP_ICON_COUNT_DISPLAY_NONE' from 3 to 4
    # The migration is to update these values.
    RealmUserDefault = apps.get_model("zerver", "RealmUserDefault")
    UserProfile = apps.get_model("zerver", "UserProfile")

    UserProfile.objects.filter(
        desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_NONE
    ).update(desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_NONE)
    RealmUserDefault.objects.filter(
        desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_NONE
    ).update(desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_NONE)

    UserProfile.objects.filter(
        desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION
    ).update(desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION)
    RealmUserDefault.objects.filter(
        desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION
    ).update(desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION)


def reverse_code(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    RealmUserDefault = apps.get_model("zerver", "RealmUserDefault")
    UserProfile = apps.get_model("zerver", "UserProfile")

    UserProfile.objects.filter(
        desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_NONE
    ).update(desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_NONE)
    RealmUserDefault.objects.filter(
        desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_NONE
    ).update(desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_NONE)

    UserProfile.objects.filter(
        desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION
    ).update(desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION)
    RealmUserDefault.objects.filter(
        desktop_icon_count_display=NEW_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION
    ).update(desktop_icon_count_display=OLD_DESKTOP_ICON_COUNT_DISPLAY_DM_MENTION)


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0489_alter_realm_can_access_all_users_group"),
    ]

    operations = [
        migrations.RunPython(renumber_options, reverse_code=reverse_code, elidable=True),
    ]
