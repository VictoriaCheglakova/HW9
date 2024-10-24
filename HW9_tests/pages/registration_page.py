import os
from datetime import datetime

from selene import be, browser, command, have

from HW9_tests.data.users import User


class RegistrationPage:

    def __init__(self):
        pass

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value).press_enter()
        return self

    def fill_second_name(self, value):
        browser.element('#lastName').should(be.blank).type(value).press_enter()
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value).press_enter()
        return self

    def choice_gender(self):
        browser.element('label[for="gender-radio-3"]').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type('4957777777')
        return self

    def fill_birthday(self, date:datetime):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('{0:%B}'.format(date))
        browser.element('.react-datepicker__year-select').type(date.year)
        browser.element(
            f'.react-datepicker__day--0{date.day}'
        ).click()
        return self

    def choice_hobbies(self):
        browser.element('label[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view)
        browser.element('label[for="hobbies-checkbox-2"]').click()
        return self

    def choice_subject(self, value):
        browser.element('#subjectsInput').type('c').click()
        browser.element('.subjects-auto-complete__input').element("//*[text()='Computer Science']").click()
        return self

    def download_picture(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))
        return self

    def fill_user_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def choise_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def choice_city(self, value):
        browser.element('#city').perform(command.js.scroll_into_view)
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def press_submit(self):
        browser.element('#submit').click()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_second_name(user.last_name)
        self.fill_email(user.email)
        self.choice_gender()
        self.fill_user_number(user.phone_number)
        self.fill_birthday(user.date)
        self.choice_subject(user.subject)
        self.choice_hobbies()
        self.download_picture(user.picture)
        self.fill_user_address(user.user_address)
        self.choise_state(user.user_state)
        self.choice_city(user.user_city)
        self.press_submit()


    def shoud_have_registered(self, ivan: User):
        browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text(f'{ivan.first_name} {ivan.last_name}'))
        browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text(ivan.email))
        browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text(ivan.gender))
        browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text(ivan.phone_number))
        browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text('{0:%d} {0:%B},{0:%Y}'.format(ivan.date)))
        browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text(ivan.subject))
        browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text(ivan.hobbies))
        browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text(ivan.picture))
        browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text(ivan.user_address))
        browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text(f'{ivan.user_state} {ivan.user_city}'))
        browser.element('#closeLargeModal').click()


