from django.db import migrations


def seed_data(apps, schema_editor):
    Course = apps.get_model('Courses', 'Course')
    Student = apps.get_model('Students', 'Student')
    Instructor = apps.get_model('Instructors', 'Instructor')

    # Courses
    python = Course.objects.create(name='Python', description='Python programming fundamentals', hours=40)
    django = Course.objects.create(name='Django', description='Web development with Django', hours=30)
    sql = Course.objects.create(name='SQL', description='Relational databases and SQL', hours=20)
    ml = Course.objects.create(name='Machine Learning', description='Intro to ML algorithms', hours=50)

    # Students
    ali = Student.objects.create(name='Ali Hassan', age=22, grade='A')
    sara = Student.objects.create(name='Sara Ahmed', age=21, grade='B+')
    omar = Student.objects.create(name='Omar Khaled', age=23, grade='A-')
    nour = Student.objects.create(name='Nour Mostafa', age=20, grade='B')
    yara = Student.objects.create(name='Yara Sami', age=22, grade='A+')

    # Enroll students in courses
    python.students.set([ali, sara, omar, yara])
    django.students.set([ali, omar, nour])
    sql.students.set([sara, nour, yara])
    ml.students.set([ali, sara, yara])

    # Instructors
    dr_amr = Instructor.objects.create(name='Dr. Amr Saleh', email='amr@iti.eg', phone='01001234567')
    dr_amr.courses.set([python, django])

    dr_hana = Instructor.objects.create(name='Dr. Hana Fathi', email='hana@iti.eg', phone='01009876543')
    dr_hana.courses.set([sql, ml])


def unseed_data(apps, schema_editor):
    Course = apps.get_model('Courses', 'Course')
    Student = apps.get_model('Students', 'Student')
    Instructor = apps.get_model('Instructors', 'Instructor')
    Instructor.objects.all().delete()
    Student.objects.all().delete()
    Course.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0002_instructor_courses'),
        ('Courses', '0002_course_students'),
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
