#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.wildberries.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='searchInput')

    # Main search field
    search_field = WebElement(css_selector='#searchInput')

    # Search button
    button_search_run = WebElement(id='applySearchBtn')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/detail.")]')

    # Button to sort products by price
    sort_products_by_price = WebElement(xpath='//*[@id="catalog_sorter"]/a[3]')

    # Button to sort products by price
    sort_products_by_sale = WebElement(xpath='//span[contains(text(),"скидке")]')

    # Button to sort products by rating
    sort_products_by_rating = WebElement(xpath='//span[contains(text(),"рейтингу")]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//*[@id="c10660421"]/div/a/div[2]/div[1]/span/ins')

    # Rating of the products in search results
    products_rating = ManyWebElements(xpath='//span[@class="product-card__count"]')

    # Button of delivery in menu
    button_of_delivery = WebElement(xpath='//a[contains(@href, "-dostavka")]')

    # Header of delivery page
    delivery_header = WebElement(xpath='//h1.c-h1')

    # Homepage link
    wildberries_link = WebElement(xpath='//img[@alt="Wildberries"]')

    # Scripts on homepage link
    homepage_banner_link = WebElement(id='app')

    # Chat icon link
    chat_icon_link = WebElement(xpath='//button[@type="button"]')

    # Chat window
    chat_window = WebElement(xpath='//div[@style="display: block;"]')

    # Advertising banner POCO
    poco_advertising = WebElement(xpath='//a[@title="Xiaomi, POCO"]')

    # One of the product card
    one_of_choose_product = WebElement(id='c91931256')

    # Price of one of the product card
    one_product_price = WebElement(css='#c91931256 .lower-price')

    # Price of product in card
    one_product_price_in_card = WebElement(css='p>span>ins.price-block__final-price')

    # Button to add to basket
    button_add_to_basket = WebElement(xpath='//body/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[9]/div[1]/div[1]/div[2]/div[1]/button[2]')

    # Basket button
    button_of_basket = WebElement(xpath='//a[contains(@href, "/lk/basket")]')

    # Message in the basket
    basket_message = WebElement(xpath='//h1[contains(text(),"В корзине пока ничего нет")]')

    # Info about product in the basket
    button_size = WebElement(xpath='//label[@class="j-size"]')

    # Info about product in the basket
    count_product_basket = WebElement(xpath='//input[@type="text"]')

    # Google play link for download
    google_play_link = WebElement(xpath='//a[contains(text(),"Загрузить из Google Play")]')

    # AppStore link for download
    app_store_link = WebElement(xpath='//a[contains(text(),"Загрузить из AppStore")]')

    # AppStore link
    app_store_text = WebElement(xpath='//a[contains(text(),"/wildberries-ooo")]')

    # AppGallery link for download
    art_gallery_link = WebElement(xpath='//a[contains(text(),"Загрузить из AppGallery")]')

    # Button delete from basket
    button_delete_from_basket = WebElement(xpath='//span[contains(text(),"Удалить")]')

    # The scope of the "to favorites" and "delete" buttons
    scope_of_delete_button = WebElement(xpath='//div[@class="list-item__wrap"]')

    # The scope of the language button
    scope_of_language_button = WebElement(xpath='//header/div[1]/div[1]/ul[1]/li[1]/span[1]')

    # Armenia button
    armenia_button = WebElement(xpath='//span[contains(text(), "Армения")]')

    # Erevan button
    erevan_button = WebElement(xpath='// div[contains(text(), "Ереван")]')

    # Sale prices of the products in search results
    sale_notes = ManyWebElements(xpath='//span[@class="spec-action__text"]')

    # Sale prices of the products in search results
    discount_product = WebElement(xpath='//span[@class="product-card__sale"]')

    # Old price of product
    old_price = WebElement(xpath='//span[@class="price-old-block"]')

    # New price of product
    new_price = WebElement(xpath='//ins[@class="lower-price"]')

    # Menu items
    menu_item = WebElement(xpath='//a[contains(@href, "/catalog")]')

    # Button menu items
    button_menu_items = WebElement(xpath='//span[@class="nav-element__burger-line"]')

    # Button menu items
    header_of_page = WebElement(xpath='/html/body/div[2]/div/div[2]/ul/li[1]/a/text()')

    # One of menu items filters
    one_of_menu_items_filters = WebElement(xpath='//label[@data-value="217"]')

    # Titles of the products in search results
    products_types = ManyWebElements(xpath='//span[@class="goods-name"]')

    # Button of address
    button_of_address = WebElement(xpath='//a[@data-wba-header-name="Pick_up_points"]')

    # Number of delivery points
    number_of_delivery_points = WebElement(css='span.count>b')

    # Number of delivery points in delivery page
    number_of_delivery_points_in_delivery = WebElement(css='div.delivery-info-item-count')

    # Button of entering
    button_of_entering = WebElement(xpath='//a[@data-wba-header-name="Login"]')

    # Entering a phone number
    entering_phone_number = WebElement(xpath='//input[@class="input-item"]')

    # Someone else's computer
    someone_computer = WebElement(xpath='//span[contains(text(), "Чужой компьютер")]')

    # Button of profile
    button_of_profile = WebElement(xpath='//a[@data-wba-header-name="LK"]')

    # Button of re-entry profile
    button_of_re_entry = WebElement(id='prevAuthBtn')

    # Button of taking code
    button_of_taking_code = WebElement(id='requestCode')

    # Link to vkontakte
    link_to_vkontakte = WebElement(xpath='//a[@class="icon-vk"]')

    # Link to youtube
    link_to_youtube = WebElement(xpath='//a[@class="icon-yt"]')

    # Link to odnoklassniki
    link_to_odnoklassniki = WebElement(xpath='//a[@class="icon-ok"]')

    # Link to telegram
    link_to_telegram = WebElement(xpath='//a[@class="icon-tg"]')

    # Link to profile
    link_to_profile = WebElement(xpath='//h2[contains(text(),"Имя не указано")]')

    # Button name change
    button_name_change = WebElement(xpath='//button[@aria-label="Изменить ФИО"]')

    # Entering last name
    entering_last_name = WebElement(id='Item.LastName')

    # Entering first name
    entering_first_name = WebElement(id='Item.FirstName')

    # Entering middle name
    entering_middle_name = WebElement(id='Item.MiddleName')

    # Save changes in profile
    save_changes = WebElement(xpath='//button[@class="btn-main"]')

    # The first name field is empty
    empty_first_name = WebElement(xpath='//span[contains(text(),"Введите имя")]')

    # The last name field is empty
    empty_last_name = WebElement(xpath='//span[contains(text(),"Введите фамилию")]')

    # Button of exit
    button_of_exit = WebElement(xpath='//a[contains(text(),"Выйти")]')

    # Favorite label 1
    favorite_label_1 = WebElement(xpath='//*[@id="c67944148"]/div/div/div/div/button')

    # Favorite label 2
    favorite_label_2 = WebElement(xpath='//*[@id="c25493589"]/div/div/div/div/button')

    # Favorite label page 1
    favorite_label_page_1 = WebElement(id='c67944148')

    # Favorite label page 2
    favorite_label_page_2 = WebElement(id='c25493589')

    # Favorite label size
    favorite_label_size = WebElement(xpath='//span[@class="sizes-list__size"]')

    # Favorite page
    favorite_page = WebElement(xpath='//span[contains(text(),"Избранное")]')

    # Items in Favorites
    items_in_favorites = ManyWebElements(xpath='//div[@class="goods-card__info-top"]')

    # Delete in Favorites
    delete_in_favorites = ManyWebElements(xpath='//span[@class="achtung-icon-white"]')

    # Item in favorite 1
    item_in_favorite_1 = WebElement(id='fav25493589')

    # Item in favorite 2
    item_in_favorite_2 = WebElement(id='fav67944148')

    # Button return to homepage
    button_return_to_homepage = WebElement(xpath='//a[contains(text(), "Перейти на главную")]')

    # A message that the code was entered incorrectly
    message_wrong_code = WebElement(xpath='//*[@id="spaAuthForm"]/div/div[3]/p[2]')

    # Icon of favorite brand
    icon_of_favorite_brand = WebElement(xpath='//a[contains(@href, "/brands/")]')

    # The field for adding a brand to favorites
    add_brand_to_favorites = WebElement(xpath='//span[@class="brand-like__text"]')

    # Favorite Brands tab
    favorite_brands_tab = WebElement(xpath='//span[contains(text(),"Любимые бренды")]')

    # Favorite Brand in special page
    favorite_elffires = WebElement(xpath='//li[@data-id="268226"]')

    # Button for delete favorite brand
    delete_favorite_elffires = WebElement(xpath='//button[contains(text(),"Удалить")]')

    # Button for returning to the brand page
    button_fo_return_brand_page = WebElement(xpath='//a[@class="btn-main"]')

    # The result of the last search
    result_last_search = WebElement(xpath='//span[contains(text(), "elffires")]')

    # Clean of the history search
    clean_result_last_search = WebElement(xpath='//button[contains(text(), "Очистить историю")]')

    # See all brands
    see_all_brands = WebElement(xpath='//span[contains(text(),"Смотреть все")]')

    # Header of the brands page
    header_of_brand_page = WebElement(xpath='//h2[@class="brands-list-page__header"]')

    # Message about wrong email
    message_wrong_email = WebElement(xpath='//p[@class="field-validation-error"]')

    # Field for inpet email
    field_put_email = WebElement(id='Item.Email')

    # Button for saving the results of email changes
    save_email_button = WebElement(xpath='//div[@class="popup__btn"]')

    # Button change of email
    button_change_email = WebElement(xpath='//button[@aria-label="Изменить адрес электронной почты"]')

    # Profile Tab
    profile_tab = WebElement(xpath='//p[@class="profile-menu__link-profile"]')

    # Email confirmation message
    conform_message = WebElement(xpath='//div[@class="div.popup-alert"]')

    # Notification page
    notification_page = WebElement(xpath='//a[@data-wba-header-name="Notifications"]')

    # Header of notification
    header_of_notification = WebElement(xpath='//li[@data-switch="apiShowEvents"]')

    # Product without any size
    product_without_size = WebElement(id='c45358316')

    # Size is sold out
    size_sold_out = WebElement(xpath='//span[contains(text(),"XXL")]')

    # Message about size sold out
    massage_out_of_sale = WebElement(xpath='//span[@class="sold-out-product__text"]')

    # Menu item shorts
    shorts_menu = WebElement(xpath='//body/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[15]/a[1]')

    # Assortment and quality link
    assortment_and_quality = WebElement(xpath='//button[@class="seo-text__button-expand"]')

    # Assortment and quality text
    assortment_and_quality_text = WebElement(xpath='//b[contains(text(),"Начни прямо сейчас!")]')

    # Checking compatibility
    check_compatibility = WebElement(xpath='//a[@class="j-wba-footer-item"]')

    # Version of my browser
    browser_version = WebElement(css_selector='div#browser-info>p>span')

    # Questions_link
    questions_link = WebElement(xpath='//li[@data-wba-footer-name="Questions"]')

    # Input for questions
    questions_input = WebElement(xpath='//*[@id="questions-answers"]/div[1]/div/input[1]')

    # Answers on questions
    answers_on_questions = ManyWebElements(css_selector='ul.j-ul-faq-search-results>li')

    # Information about cookies
    cookies_status = WebElement(xpath='//tbody/tr[1]/td[3]/span[1]')

    # Information about js
    js_status = WebElement(xpath='//tbody/tr[2]/td[3]/span[1]')

    # Icon for img download
    icon_img_download = WebElement(id='searchByImageContainer')

    # Button for img download
    button_img_download = WebElement(xpath='//label[@class="upload-photo-btn"]')

    # Header of photo search
    header_of_photo_search = WebElement(xpath='//h1[@class="searching-results__title"]')

    # Button of report a problem
    button_report_problem = WebElement(xpath='//header/div[1]/div[1]/button[1]')

    # Field for chatting with bot
    field_for_chatbot = WebElement(xpath='//textarea[@class="chat__textarea"]')

    # Close window of chatbot
    close_window_bot = WebElement(xpath='//button[@class="chat__btn-close"]')

    # Delete previous request button
    delete_previous_report = WebElement(xpath='//header/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]')
























































































































