#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#


import pytest
import time
from pages.wildberries import MainPage
import pyautogui


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 41

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'elffires' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "ботинки" with English keyboard:
    page.search = ',jnbyrb'
    page.button_search_run.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 105

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'ботинки' in title.lower(), msg


@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.

        Note: this test case will fail because there is a bug in
               sorting products by price.
    """

    page = MainPage(web_browser)

    page.search = 'женские футболки'
    page.button_search_run.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.wait_page_loaded()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()

    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', ' ')) for p in all_prices]

    print(all_prices)
    sorted_all_prices = (sorted(all_prices))

    # Make sure products are sorted by price correctly:
    assert all_prices != sorted_all_prices, "Sort by price doesn't work!"


def test_delivery(web_browser):
    """ Make sure that clicking on the delivery link. """
    page = MainPage(web_browser)

    page.button_of_delivery.click()

    # Make sure user place at the needs pages
    for title in page.delivery_header.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Доставка' in title.lower(), msg


def test_check_return_to_the_main_page(web_browser):
    """ Make sure main Wildberries link is working. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wildberries_link.click()

    # Make sure banner is visible so we return to homepage
    assert page.homepage_banner_link.is_visible(), "Failed to return to the start page"


def test_check_chat_ivon(web_browser):
    """ Make sure chat icon is working. """

    page = MainPage(web_browser)

    page.chat_icon_link.click()

    # Make sure chat window is visible
    assert page.chat_window.is_visible(), "Chat window is not visible"


def test_check_poco_adverticing_banner(web_browser):
    """ Make sure that adverticing banner is working. """

    page = MainPage(web_browser)

    page.poco_advertising.click()

    # Make sure user place at the needs pages
    for title in page.delivery_header.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'POCO' in title.lower(), msg


def test_check_try_to_add_into_basket_without_size(web_browser):
    """ Make sure without choosing size,
    the item is not added to the basket. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()
    page.one_of_choose_product.click()
    page.button_add_to_basket.click()

    # Open the basket
    page.button_of_basket.click()
    page.wait_page_loaded()

    # Make sure without choosing the size, the item is not added to the basket
    assert page.basket_message.is_visible(), 'Basket is not empty'


def test_check_price_comparison(web_browser):
    """ Make sure the price of the product in the search and the card is the same. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    price_elffires = page.one_product_price.get_text()

    page.one_of_choose_product.click()
    page.wait_page_loaded()

    price_elffires_in_card = page.one_product_price_in_card.get_text()

    # Make sure prices are the same
    assert price_elffires == price_elffires_in_card, 'Something wrong with price of product'


def test_check_try_to_add_into_basket_with_size(web_browser):
    """ Make sure with choosing size, the item is added to the basket. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    # Open the product card
    page.one_of_choose_product.click()
    page.button_size.click()
    page.button_add_to_basket.click()

    # Open the basket
    page.button_of_basket.click()
    page.wait_page_loaded()

    # Make sure with choosing size, the item is added to the basket
    assert page.count_product_basket.get_text() != 0, 'Basket is empty'


# @pytest.mark.xfail(reason="Google play link is not working")
def test_check_google_play_link(web_browser):
    """ Make sure that google play link is working.

        Note: this test case will fail because
        google play may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://play.google.com/store/apps/details?id=com.wildberries.ru'

    # Try to open appstore
    page.google_play_link.click()  # Клик на ссылку скачивания
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Google play link is not working'


# @pytest.mark.xfail(reason="Appstore link is not working")
def test_check_app_store_link(web_browser):
    """ Make sure that appstore link is working.

        Note: this test case will fail because
        appstore may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()

    original_window = 'https://apps.apple.com/ru/app/wildberries/id597880187'
    # Try to open google play
    page.app_store_link.click()  # Клик на ссылку скачивания
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Appstore link is not working'


# @pytest.mark.xfail(reason="Artgallery link is not working")
def test_check_art_gallery_link(web_browser):
    """ Make sure that artgallery link is working.

        Note: this test case will fail because
        artgallery may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://appgallery.huawei.com/#/app/C101183325'

    # Try to open artgallery
    page.art_gallery_link.click()
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Artgallery link is not working'


def test_check_delete_from_basket(web_browser):
    """ Make sure that product can be delete from basket."""

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    # Open the product card
    page.one_of_choose_product.click()
    page.button_size.click()

    # Add product to the basket
    page.button_add_to_basket.click()

    page.button_of_basket.click()

    # Move the cursor for the delete button to appear
    page.scope_of_delete_button.move_to_element()

    # Delete product from the basket
    page.button_delete_from_basket.click()

    # Make sure the item was deleted to the basket
    assert page.basket_message.is_visible(), 'Basket is not empty'


def test_check_change_language(web_browser):
    """ Make sure when the language changes, the geolocation changes."""

    page = MainPage(web_browser)

    # Move the cursor for the delete button to appear
    page.scope_of_language_button.move_to_element()
    page.armenia_button.click()
    page.wait_page_loaded()

    # Make sure the geolocation changes
    assert page.erevan_button.is_visible(), 'The geolocation not changes'


def test_check_correctly_discount_price(web_browser):
    """ Make sure price with the discount is considered correct."""

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()

    page.sort_products_by_sale.click()
    page.wait_page_loaded()

    discount = page.discount_product.get_text()

    # Get the discount amount without extra characters
    discount = int(discount[1:3])
    old_price = page.old_price.get_text()

    # Get the old price without extra characters
    old_price = int(old_price[0:1]+old_price[2:5])
    new_price = (page.new_price.get_text())

    # Get the new price without extra characters
    new_price = int(new_price[:3])

    discount_price = round(old_price*(discount/100))

    # Make sure price with the discount is considered correct
    assert old_price-discount_price == new_price, 'Discount is not right'


def test_check_menu_items_work(web_browser):
    """ Make sure menu items work correctly."""   # Доработать, чтобы проверялись все менюшки

    page = MainPage(web_browser)

    page.button_menu_items.click()

    page.menu_item.click()
    print(f'Header of page = {page.header_of_page}')

    # Make sure user place at the needs pages
    for title in page.delivery_header.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Женщинам' in title.lower(), msg


@pytest.mark.xfail(reason="Filter by rating doesn't work")
def test_check_sort_by_rating(web_browser):
    """ Make sure that sort by rating works fine.

        Note: this test case will fail because there is a bug in
               sorting products by ratings.
    """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_rating.scroll_to_element()
    page.wait_page_loaded()
    page.sort_products_by_rating.click()
    page.wait_page_loaded()

    # Get ratings of the products in Search results
    all_ratings = page.products_rating.get_text()

    # Convert all ratings from strings to numbers
    all_ratings = [int(p.replace(' ', ' ')) for p in all_ratings]

    sorted_all_ratings = sorted(all_ratings)

    # Make sure products are sorted by price correctly:
    assert all_ratings != sorted_all_ratings, "Sort by ratings doesn't work!"


def test_check_filter_is_working(web_browser):
    """ Make sure filtering works."""

    page = MainPage(web_browser)

    page.search = 'куякъ'
    page.button_search_run.click()
    page.one_of_menu_items_filters.click()
    page.wait_page_loaded()

    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'лонгслив' in title.lower(), msg


def test_check_count_of_pick_up_points(web_browser):
    """ The information about the pick-up points is the same."""

    page = MainPage(web_browser)

    # Move the cursor for the delete button to appear
    page.button_of_address.move_to_element()

    # Get the number of output items in the drop-down menu
    number_of_points = page.number_of_delivery_points.get_text()
    number_of_points = number_of_points[1:2]+number_of_points[3:6]

    page.button_of_address.click()
    number_of_points_in_delivery = page.number_of_delivery_points_in_delivery.get_text()
    number_of_points_in_delivery = number_of_points_in_delivery[1:2]+number_of_points_in_delivery[3:6]

    assert number_of_points == number_of_points_in_delivery, 'The data on the pick-up points not match'


@pytest.mark.xfail(reason="The code does not have time to arrive")
def test_check_first_log_in_profile(web_browser):
    """ Make sure first login to the account is working.

        Note: this test case will fail because the entry has already been made earlier
        or the code does not have time to arrive
    """

    page = MainPage(web_browser)

    page.button_of_entering.click()
    page.entering_phone_number.click()
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    assert page.button_of_profile.is_visible(), 'Problems logging in to account'


@pytest.mark.xfail(reason="The code was not entered")
def test_check_enter_wrong_code(web_browser):
    """ Make sure can not log in, when input the wrong code.

        Note: this test case will fail because the entry has already been made earlier
        or the code does not have time to arrive
    """

    page = MainPage(web_browser)

    page.button_of_entering.click()
    page.entering_phone_number.click()
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(5)

    assert page.message_wrong_code.is_visible(), 'There is no information about the introduction of an erroneous code'


@pytest.mark.xfail(reason="The first login to the account")
def test_check_log_in_profile(web_browser):
    """ Make sure login to the account is working.
        Note: this test case will fail because it is the first login to the account.
    """

    page = MainPage(web_browser)

    page.button_of_entering.click()
    page.someone_computer.click()
    page.button_of_re_entry.click()

    assert page.button_of_profile.is_visible(), 'Problems logging in to your account'


@pytest.mark.xfail(reason="Vk link is not working")
def test_check_vk_link(web_browser):
    """ Make sure that vk link is working.

        Note: this test case will fail because
        vk may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://vk.com/public9695053'

    # Try to open vk
    page.link_to_vkontakte.click()
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Vk link is not working'


@pytest.mark.xfail(reason="Youtube link is not working")
def test_check_youtube_link(web_browser):
    """ Make sure that youtube link is working.

        Note: this test case will fail because
        youtube may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://www.youtube.com/Wildberriesshop'

    # Try to open youtube
    page.link_to_youtube.click()
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Youtube link is not working'


@pytest.mark.xfail(reason="Odnoklassniki link is not working")
def test_check_odnoklassniki_link(web_browser):
    """ Make sure that odnoklassniki link is working.

        Note: this test case will fail because
        odnoklassniki may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://ok.ru/wildberries'

    # Try to open odnoklassniki
    page.link_to_odnoklassniki.click()
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Odnoklassniki link is not working'


@pytest.mark.xfail(reason="Telegram link is not working")
def test_check_telegram_link(web_browser):
    """ Make sure that telegram link is working.

        Note: this test case will fail because
        telegram may have problems downloading.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    original_window = 'https://t.me/wildberriesru_official'

    # Try to open telegram
    page.link_to_telegram.click()
    page.switch_to_window(1)
    window_after = page.get_current_url()

    # Make sure link open right
    assert original_window == window_after, 'Telegram link is not working'


@pytest.mark.xfail(reason="Registration without a last name is allowed!")
def test_check_profile_changes_without_last_name(web_browser):
    """ Make sure we can't change profile without last name.

        Note: this test case will fail because the authorization code has not been entered,
        registration without a last name is allowed on the site.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.click()
    page.link_to_profile.click()
    page.button_name_change.click()

    # Enter everything except the last name
    page.entering_first_name.click()
    page.entering_first_name = 'Лиса'
    page.entering_middle_name.click()
    page.entering_middle_name = 'Алиса'

    # Try to save changes
    page.save_changes.click()

    # Make sure is not allowed to enter without a last name
    assert page.empty_last_name.is_visible(), 'It is allowed to enter without a last name'


@pytest.mark.xfail(reason="Registration without a first name is allowed!")
def test_check_profile_changes_without_first_name(web_browser):
    """ Make sure we can't change profile without first name.

        Note: this test case will fail because the authorization code has not been entered,
        registration without a first name is allowed on the site.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.click()
    page.link_to_profile.click()
    page.button_name_change.click()

    # Enter everything except the last name
    page.entering_last_name.click()
    page.entering_last_name = 'Алиса'
    page.entering_middle_name.click()
    page.entering_middle_name = 'Лиса'

    # Try to save changes
    page.save_changes.click()

    # Make sure is not allowed to enter without a first name
    assert page.empty_first_name.is_visible(), 'It is allowed to enter without a first name'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_successful_profile_changes(web_browser):
    """ Make sure we can't change profile without first name.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.click()
    page.link_to_profile.click()
    page.button_name_change.click()

    # Enter everything except the last name
    page.entering_last_name.click()
    page.entering_last_name = 'Лиса'
    page.entering_first_name.click()
    page.entering_first_name = 'Алиса'

    # Try to save changes
    page.save_changes.click()

    # Make sure is not allowed to enter without a first name
    assert page.empty_first_name.is_visible() == False, 'The profile change was not successful'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_add_items_to_favorites(web_browser):
    """ Make sure you have added all the items to your favorites.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Find something in search
    page.search = 'elffires'
    page.button_search_run.click()

    # Add two first element in favorite
    page.favorite_label_page_1.move_to_element()
    page.favorite_label_1.click()
    page.favorite_label_size.click()
    page.favorite_label_page_2.move_to_element()
    page.favorite_label_2.click()
    page.favorite_label_size.click()

    # Go to favorites
    page.button_of_profile.move_to_element()
    page.favorite_page.click()

    product_favorite = page.items_in_favorites.get_text()
    product_favorite = len(product_favorite)

    # Make sure you have added all the items to your favorites
    assert product_favorite == 2, 'Adding to favorites does not work'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_delete_items_to_favorites(web_browser):
    """ Make sure you have delete all the items in your favorites.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Go to favorites
    page.button_of_profile.move_to_element()
    page.favorite_page.click()

    page.item_in_favorite_1.move_to_element()
    page.delete_in_favorites[0].click()
    page.item_in_favorite_2.move_to_element()
    page.delete_in_favorites[0].click()

    # Make sure you have added all the items to your favorites
    assert page.button_return_to_homepage.is_visible(), 'Delete from favorites does not work'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_add_items_to_basket_with_log_in(web_browser):
    """ Make sure you have added items to your basket with log in.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    # Open the product card
    page.one_of_choose_product.click()
    page.button_size.click()
    page.button_add_to_basket.click()

    # Open the basket
    page.button_of_basket.click()
    page.wait_page_loaded()

    # Make sure with choosing size, the item is added to the basket
    assert page.count_product_basket.get_text() != 0, 'Basket is empty'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_delete_items_to_basket_with_log_in(web_browser):
    """ Make sure you have delete items to your basket with log in.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Open the basket
    page.button_of_basket.click()
    page.wait_page_loaded()

    # Move the cursor for the delete button to appear
    page.scope_of_delete_button.move_to_element()

    # Delete product from the basket
    page.button_delete_from_basket.click()

    # Make sure the item was deleted to the basket
    assert page.basket_message.is_visible(), 'Basket is not empty'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_add_brand_to_favorites(web_browser):
    """ Make sure add brand to your favorites is working.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    page.icon_of_favorite_brand.click()
    page.add_brand_to_favorites.click()
    page.button_of_profile.move_to_element()
    page.favorite_brands_tab.click()

    assert page.favorite_elffires.is_visible(), 'Adding to favorites brand is not working'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_delete_brand_to_favorites(web_browser):
    """ Make sure delete brand to your favorites is working.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    page.button_of_profile.move_to_element()
    page.favorite_brands_tab.click()
    page.icon_of_favorite_brand.move_to_element()
    page.delete_favorite_elffires.click()

    assert page.button_fo_return_brand_page.is_visible(), 'Delete to favorites brand is not working'


def test_check_result_ot_the_last_search(web_browser):
    """ Make sure delete brand to your favorites is working."""

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()

    page.go_back()
    page.search_field.click()
    page.result_last_search.click()

    # Make sure user place at the needs pages
    for title in page.header_of_page.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'elffires' in title.lower(), msg


def test_check_delete_result_ot_the_last_search(web_browser):
    """ Make sure delete result of the last search is working."""

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()

    page.go_back()
    page.search_field.click()

    # Clean the search history
    page.clean_result_last_search.click()

    # Make sure the last search point is not visible
    assert page.result_last_search.is_visible() == False, 'Clean search history is not working'


def test_check_button_of_all_brands(web_browser):
    """ Make sure button of all brands is working."""

    page = MainPage(web_browser)

    # Scroll page to our element
    page.see_all_brands.scroll_to_element()
    page.see_all_brands.click()

    # Save the url of the page we are going to
    new_page = page.get_current_url()

    # Save the desired page to a variable
    brands_url = 'https://www.wildberries.ru/brandlist/all'

    # Make sure the variables match
    assert new_page == brands_url, 'The transition to the brands page did not occur'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_wrong_email_not_save(web_browser):
    """ Make sure we can't change email with wrong format.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.move_to_element()
    page.profile_tab.click()
    page.button_change_email.click()

    # Enter wrong email format
    page.field_put_email.click()
    page.field_put_email = '123'

    # Try to save changes
    page.save_email_button.click()

    # Make sure is not allowed to enter with wrong email format
    assert page.field_put_email.is_visible(), 'The email change was successful with wrong format of email'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_email_save(web_browser):
    """ Make sure we can change email.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.move_to_element()
    page.profile_tab.click()
    page.button_change_email.click()

    # Enter wrong email format
    page.field_put_email.click()
    page.field_put_email = 'maria_poly527@list.ru'

    # Try to save changes
    page.save_email_button.click()

    # Make sure is not allowed to enter with wrong email format
    assert page.conform_message.is_visible(), 'The email change was not successful'


@pytest.mark.xfail(reason="Registration has problem with authorization code!")
def test_check_link_of_notification(web_browser):
    """ Make sure link of notification is working.

        Note: this test case will fail because the authorization code has not been entered.
    """

    page = MainPage(web_browser)

    # Login in account
    page.button_of_entering.click()
    page.entering_phone_number.click()

    # Imitating keyboard input
    pyautogui.typewrite('9102427790')
    page.someone_computer.click()
    page.button_of_taking_code.click()
    time.sleep(20)

    # Enter the profile
    page.button_of_profile.move_to_element()
    page.notification_page.click()

    assert page.header_of_notification.is_presented(), 'Link of notification is not working'


def test_check_try_add_product_with_size_sold_out(web_browser):
    """ Make sure product without any size can not be add in basket. """

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()
    page.product_without_size.click()
    page.size_sold_out.click()

    # Make sure without choosing the size, the item is not added to the basket
    assert page.massage_out_of_sale.is_presented(), 'You can add an item with a sold-out size to the basket'


def test_check_next_menu_items_work(web_browser):
    """ Make sure next menu items work correctly."""

    page = MainPage(web_browser)

    page.button_menu_items.click()

    page.menu_item.move_to_element()
    page.shorts_menu.click()

    # Make sure user place at the needs pages
    for title in page.delivery_header.get_text():
        msg = 'Wrong header in page "{}"'.format(title)
        assert 'Шорты' in title.lower(), msg


def test_check_link_full_text(web_browser):
    """ Make sure link to expand the full text does work."""

    page = MainPage(web_browser)

    page.scroll_down()
    page.assortment_and_quality.click()
    page.wait_page_loaded()

    # Make sure clicking on the link opened the full text
    assert page.assortment_and_quality_text.is_visible(), 'The link to expand the full text does not work'


def test_check_version_of_browser(web_browser):
    """ Make sure the browser versions specified in the browser itself and on the site are the same."""

    page = MainPage(web_browser)

    # Specify the version of my browser
    my_browser = 'Google Chrome 103.0.5060.134'

    page.scroll_down()
    page.check_compatibility.click()
    version_of_browser = page.browser_version.get_text()
    print(f'Version of browser = {version_of_browser}')

    assert my_browser == version_of_browser, 'Versions browser are not the same'


@pytest.mark.xfail(reason="The text field is protected from automatic input!")
def test_check_questions_input(web_browser):
    """ Make sure that the specified phrase is present in the answers.

    Note: this test case will fail because the text field can be protected from automatic input.
    """

    page = MainPage(web_browser)

    page.scroll_down()
    page.questions_link.click()
    page.wait_page_loaded()
    page.questions_input.click()
    page.questions_input = 'как вернуть товар'

    # Make sure that the specified phrase is present in the answers
    for answer in page.answers_on_questions.get_text():
        msg = 'Wrong header in page "{}"'.format(answer)
        assert 'вернуть' in answer.lower(), msg


def test_check_basket_to_homepage(web_browser):
    """ Make sure that button 'back to homepage' in basket is working."""

    page = MainPage(web_browser)

    page.button_of_basket.click()
    page.wait_page_loaded()
    page.button_return_to_homepage.click()
    wilb_url ='https://www.wildberries.ru/'

    assert page.get_current_url() == wilb_url, 'Button is not working'


def test_check_cookies_js_work(web_browser):
    """ Make sure cookies and js are working."""

    page = MainPage(web_browser)

    page.scroll_down()
    page.check_compatibility.click()

    assert page.cookies_status.get_text() == 'Вкл', 'Cookies are not working'
    assert page.js_status.get_text() == 'Вкл', 'Js are not working'


def test_check_search_to_img(web_browser):
    """ Make sure photo search is working."""

    page = MainPage(web_browser)

    page.icon_img_download.click()
    page.button_img_download.click()

    # Time is given to have time to select and upload an image
    time.sleep(10)

    assert page.header_of_photo_search.is_visible(), 'Photo search did not work'


def test_check_report_a_problem(web_browser):
    """ Make sure button of report a problem open a chat."""

    page = MainPage(web_browser)

    page.button_report_problem.click()

    assert page.chat_window.is_visible(), 'Button of report a problem does not open a chat'


def test_check_delete_previously_report(web_browser):
    """ Make sure you can delete one of the previously made requests."""

    page = MainPage(web_browser)

    page.search = 'elffires'
    page.button_search_run.click()
    page.wait_page_loaded()
    page.search = 'witcher'
    page.button_search_run.click()
    page.wait_page_loaded()
    page.search = 'anime'
    page.button_search_run.click()
    page.wait_page_loaded()

    page.search_field.click()
    page.delete_previous_report.click()

    assert page.delete_previous_report.is_visible() == False, 'Not working'










