import os

from selene import be, browser, command, have


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

    def fill_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
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

    def shoud_have_registered(self, full_name, email, gender, number, date_of_birth, subject, hobbies, path_of_picture, address, state_city):
        browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text(full_name))
        browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text(email))
        browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text(gender))
        browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text(number))
        browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text(date_of_birth))
        browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text(subject))
        browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text(hobbies))
        browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text(path_of_picture))
        browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text(address))
        browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text(state_city))
        browser.element('#closeLargeModal').click()


