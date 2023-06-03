from selenium.webdriver.common.by import By


class FormPageLocators:
    # ФОРМИ(ФУНКЦІОНАЛ): ПОШУК, КОШИК, КУПІВЛЯ,ВИДАЛЕННЯ З КОШИКА
    SEARCH_PRODUCT = (By.ID, 'search-form__input')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'button[class*="search-form__submit-button"]')
    NEXT_PRODUCT = (By.CSS_SELECTOR,  'a[href="https://allo.ua/ua/products/mobile/samsung-galaxy-a34-6-128-sm-a346ezkasek-black.html"')
    BUY = (By.ID, 'product-buy-button')
    ORDER_FORM = (By.CLASS_NAME, 'order-now')
    LOGOS_ALLO = (By.XPATH, '//*[@id="__layout"]/div/header/div[1]/a/img')
    BASKET = (By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[2]/button')
    DELETE_PRODUCT = (By.CSS_SELECTOR, 'svg[class*="vi i-shared vi__close remove"]')
    CLOSE_WINDOW = (By.CSS_SELECTOR, 'svg[class*="vi i-shared vi__close"]')

    # Проводимо авторизацію без введення даних(без вводу номеру, введення дійсного номеру, але не зареєстрованого)
    AUTHORIZATION = (By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[1]/button')
    NUMBER_CLICK = (By.CSS_SELECTOR, 'button[class*="a-button a-button--block a-button--lg a-button--primary"]')
    NUMBER_PHONE = (By.NAME, 'telephone')
    # СПРОБА АВТОРИЗАЦІЇ ЧЕРЕЗ "ІНШИЙ СПОСІБ ВХОДУ" (EMAIL
    ANOTHER_METHOD = (By.CLASS_NAME, 'a-button__text')
    EMAIL_LOGIN = (By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[1]/button')






    # КАТАЛОГ
    CLOSES = (By.CSS_SELECTOR, '')
    BAGS = (By.CSS_SELECTOR, '')
    SHOES = (By.CSS_SELECTOR, '')
    ACCESSORY = (By.CSS_SELECTOR, '')
    NOVELTY = (By.CSS_SELECTOR, '')
    DISCOUNTS = (By.CSS_SELECTOR, '')
    FINAL_SALE = (By.CSS_SELECTOR, '')
    LEADER_SALES = (By.CSS_SELECTOR, '')
