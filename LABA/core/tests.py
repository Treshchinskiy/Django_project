from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Employee, Admin, Zakazchik
from datetime import date

User = get_user_model()




class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            date_of_birth=date(1990, 1, 1),
            address='123 Test St',
            number='1234567890',
            has_rewiews=True
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.address, '123 Test St')
        self.assertEqual(self.user.number, '1234567890')
        self.assertTrue(self.user.has_rewiews)

    def test_user_age(self):
        self.assertEqual(self.user.age, date.today().year - 1990)



class EmployeeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='employeeuser', password='password123')
        self.employee = Employee.objects.create(
            user_id=self.user,
            position='Developer',
            salary=60000.0,
            hire_date=date(2020, 1, 1)
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.user_id.username, 'employeeuser')
        self.assertEqual(self.employee.position, 'Developer')
        self.assertEqual(self.employee.salary, 60000.0)
        self.assertEqual(self.employee.hire_date, date(2020, 1, 1))

    def test_employee_str(self):
        self.assertEqual(str(self.employee), 'employeeuser')



class ZakazchikModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='zakazchikuser', password='password123')
        self.zakazchik = Zakazchik.objects.create(
            user=self.user,
            amount_zakazov=5
        )

    def test_zakazchik_creation(self):
        self.assertEqual(self.zakazchik.user.username, 'zakazchikuser')
        self.assertEqual(self.zakazchik.amount_zakazov, 5)

    



class AdminModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adminuser', password='password123')
        self.admin = Admin.objects.create(
            user_id=self.user,
            salary=80000.0,
            position='MAIN ADMIN'
        )

    def test_admin_creation(self):
        self.assertEqual(self.admin.user_id.username, 'adminuser')
        self.assertEqual(self.admin.salary, 80000.0)
        self.assertEqual(self.admin.position, 'MAIN ADMIN')

    def test_admin_str(self):
        self.assertEqual(str(self.admin), 'adminuser')
