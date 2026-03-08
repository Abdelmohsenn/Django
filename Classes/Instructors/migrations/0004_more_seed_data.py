from django.db import migrations


def seed_more(apps, schema_editor):
    Course = apps.get_model('Courses', 'Course')
    Student = apps.get_model('Students', 'Student')
    Instructor = apps.get_model('Instructors', 'Instructor')

    # More Courses
    html = Course.objects.create(name='HTML & CSS', description='Frontend web design basics', hours=20)
    js = Course.objects.create(name='JavaScript', description='Dynamic web programming', hours=35)
    ds = Course.objects.create(name='Data Structures', description='Arrays, trees, graphs and algorithms', hours=45)
    dl = Course.objects.create(name='Deep Learning', description='Neural networks and deep learning', hours=60)
    devops = Course.objects.create(name='DevOps', description='CI/CD, Docker and cloud deployment', hours=30)

    # More Students
    karim = Student.objects.create(name='Karim Nabil', age=24, grade='B+')
    lina = Student.objects.create(name='Lina Tarek', age=21, grade='A')
    hassan = Student.objects.create(name='Hassan Magdy', age=25, grade='B')
    dina = Student.objects.create(name='Dina Sherif', age=22, grade='A-')
    mostafa = Student.objects.create(name='Mostafa Adel', age=23, grade='A+')
    rania = Student.objects.create(name='Rania Youssef', age=20, grade='B+')

    # Enroll students
    html.students.set([lina, dina, rania, karim])
    js.students.set([karim, lina, mostafa, dina])
    ds.students.set([hassan, mostafa, karim])
    dl.students.set([mostafa, dina, rania])
    devops.students.set([hassan, karim, mostafa])

    # More Instructors
    dr_tamer = Instructor.objects.create(name='Dr. Tamer Nour', email='tamer@iti.eg', phone='01112223344')
    dr_tamer.courses.set([html, js])

    dr_mariam = Instructor.objects.create(name='Dr. Mariam Lotfy', email='mariam@iti.eg', phone='01223334455')
    dr_mariam.courses.set([ds, dl])

    dr_wael = Instructor.objects.create(name='Dr. Wael Samir', email='wael@iti.eg', phone='01334445566')
    dr_wael.courses.set([devops])


def unseed_more(apps, schema_editor):
    Course = apps.get_model('Courses', 'Course')
    Student = apps.get_model('Students', 'Student')
    Instructor = apps.get_model('Instructors', 'Instructor')
    extra_courses = ['HTML & CSS', 'JavaScript', 'Data Structures', 'Deep Learning', 'DevOps']
    extra_students = ['Karim Nabil', 'Lina Tarek', 'Hassan Magdy', 'Dina Sherif', 'Mostafa Adel', 'Rania Youssef']
    extra_instructors = ['Dr. Tamer Nour', 'Dr. Mariam Lotfy', 'Dr. Wael Samir']
    Instructor.objects.filter(name__in=extra_instructors).delete()
    Student.objects.filter(name__in=extra_students).delete()
    Course.objects.filter(name__in=extra_courses).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0003_seed_data'),
    ]

    operations = [
        migrations.RunPython(seed_more, unseed_more),
    ]
