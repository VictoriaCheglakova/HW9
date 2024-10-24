from HW9_tests.pages.registration_page import RegistrationPage


def test_registration_user(open_browser):
    registration_page = RegistrationPage()

    (
        registration_page
        .fill_first_name('Иван')
        .fill_second_name('Иванов')
        .fill_email('ivanov@gmail.com')
        .choice_gender()
        .fill_user_number('4957777777')
        .fill_birthday('July', '1930', '10')
        .choice_hobbies()
        .choice_subject('Computer Science')
        .download_picture('cat.jpg')
        .fill_user_address('Простоквашино, д. 1')
        .choise_state('Haryana')
        .choice_city('Karnal')
        .press_submit()

    )
    registration_page.shoud_have_registered ('Иван Иванов','ivanov@gmail.com', 'Other',
                                             '4957777777','10 July,1930', 'Computer Science', 'Reading', 'cat.jpg',
                                             'Простоквашино, д. 1', 'Haryana Karnal' )

