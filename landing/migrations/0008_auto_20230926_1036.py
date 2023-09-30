from django.db import migrations
import uuid, random, string

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("landing", "User")
    for row in MyModel.objects.all():
        row.uuid = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=13))
        row.save(update_fields=["fidc"])


class Migration(migrations.Migration):
    dependencies = [
        ("landing", "0007_user_fidc"),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]