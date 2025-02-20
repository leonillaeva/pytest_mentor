from auction_project.pages.base_page import BasePage
from selenium import webdriver
from auction_project.creds import BASE_URL
from auction_project.locators.locators import LocatorHomePage, LocatorLoginPage, LocatorAccountSettings


class LoginPage(BasePage):
    pass


if __name__ == "__main__":
    driver = webdriver.Chrome()
    lg_pg = LoginPage(driver)

    lg_pg.open_page(BASE_URL)
    home_sign_in = lg_pg.search_element(LocatorHomePage.HOME_SIGNIN_BUTTON)
    lg_pg.click_element(home_sign_in)

    login_signin = lg_pg.search_element(LocatorLoginPage.LOGIN_SIGNIN_BUTTON)
    lg_pg.click_element(login_signin)

    mod_win = lg_pg.search_element(LocatorLoginPage.DIALOG_MODAL_WINDOW)
    # if mod_win:
    #     print("Modal window is found")
    # else:
    #     print('Modal window is not found')
    win_description = lg_pg.search_element(LocatorLoginPage.WINDOW_DESCRIPTION).text
    # print(win_description)

    forgot_password_link = lg_pg.search_element(LocatorLoginPage.WINDOW_FORGOT_PASSWORD_LINK_TEXT)
    # print(forgot_password_link.get_attribute("href"))

    red_x_icon_block = lg_pg.search_element(LocatorLoginPage.RED_X_BUTTON_MODAL_WINDOW)
    red_x_icon_content = lg_pg.get_property_value_execute_script(red_x_icon_block,
                                                                 "::before",
                                                                 "content")

    print(red_x_icon_content)
