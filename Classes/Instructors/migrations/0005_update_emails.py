from django.db import migrations


EMAIL_MAP = {
    'Dr. Amr Saleh':   'amr.saleh@stanford.edu',
    'Dr. Hana Fathi':  'hana.fathi@stanford.edu',
    'Dr. Tamer Nour':  'tamer.nour@stanford.edu',
    'Dr. Mariam Lotfy':'mariam.lotfy@stanford.edu',
    'Dr. Wael Samir':  'wael.samir@stanford.edu',
}


def update_emails(apps, schema_editor):
    Instructor = apps.get_model('Instructors', 'Instructor')
    for name, email in EMAIL_MAP.items():
        Instructor.objects.filter(name=name).update(email=email)


def revert_emails(apps, schema_editor):
    OLD_MAP = {
        'Dr. Amr Saleh':   'amr@iti.eg',
        'Dr. Hana Fathi':  'hana@iti.eg',
        'Dr. Tamer Nour':  'tamer@iti.eg',
        'Dr. Mariam Lotfy':'mariam@iti.eg',
        'Dr. Wael Samir':  'wael@iti.eg',
    }
    Instructor = apps.get_model('Instructors', 'Instructor')
    for name, email in OLD_MAP.items():
        Instructor.objects.filter(name=name).update(email=email)


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0004_more_seed_data'),
    ]

    operations = [
        migrations.RunPython(update_emails, revert_emails),
    ]
