import datetime

from HW9_tests.data.users import User
from HW9_tests.pages.registration_page import RegistrationPage


def test_registration_user(open_browser):
    registration_page = RegistrationPage()
    date = datetime.datetime(1930, 7, 10)

    user_ivan = User('Иван', 'Иванов', 'ivanov@gmail.com', '4957777777', date, 'Computer Science',
                      'cat.jpg', 'Простоквашино, д. 1', 'Haryana', 'Karnal', 'Other', 'Reading')

    registration_page.register(user_ivan)

    registration_page.shoud_have_registered(user_ivan)


