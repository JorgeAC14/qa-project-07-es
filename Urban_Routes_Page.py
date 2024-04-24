import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    # Ubicaciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Seleccionar taxi
    taxi_button = (By.CSS_SELECTOR, '.results-container .button.round')
    comfort_tariff_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    # Número de teléfono
    phone_number = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, '.buttons .button.full')
    sms_code_field = (By.ID, 'code')
    sms_confirm_button = (By.XPATH, "//button[text()='Confirmar']")

    # Método de pago
    payment_method_button = (By.CLASS_NAME, 'pp-value-container')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    cvv_field = (By.XPATH, "//input[@class='card-input' and @id='code']")
    cambio_enfoque = (By.CLASS_NAME, 'card-wrapper')
    add_button = (By.XPATH, "//button[text()='Agregar']")
    close_button_card = (By.XPATH,
                         "//div[contains(@class, 'payment-picker') and contains(@class, 'open')]//div[contains("
                         "@class, 'modal')]//div[contains(@class, 'section') and contains(@class, 'active')]//button["
                         "contains(@class, 'close-button') and contains(@class, 'section-close')]")

    # Mensaje
    message_field = (By.ID, 'comment')

    # Pedir manta y pañuelos
    blanket_tissue_slider = (By.XPATH,
                             "//div[@class='r-sw-container' and div[@class='r-sw-label' and text()='Manta y "
                             "pañuelos']]//span[@class='slider round']")

    # Pedir helado
    order_ice_creams_button = (By.CLASS_NAME, "counter-plus")
    ice_creams_disabled = (By.CLASS_NAME, "counter-minus disabled")
    ice_cream_count = (By.XPATH,
                       "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div["
                       "@class='r-counter']//div[@class='counter-value' and text()='2']")

    # Pedir taxi
    confirm_taxi = (By.CLASS_NAME, "smart-button-secondary")

    # Información del conductor en el modal
    driver_information_modal = (By.CLASS_NAME, "order-header-title")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_taxi(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.taxi_button))
        self.driver.find_element(*self.taxi_button).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()

    def click_phone_number(self):
        self.driver.find_element(*self.phone_number).click()

    def fill_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.next_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def fill_sms_code(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.sms_code_field))
        self.driver.find_element(*self.sms_code_field).send_keys(helpers.retrieve_phone_code(self.driver))
        self.driver.find_element(*self.sms_confirm_button).click()

    def get_sms_code(self):
        return self.driver.find_element(*self.sms_code_field).get_property('value')

    def add_credit_card(self, card_number, card_code):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.payment_method_button))
        self.driver.find_element(*self.payment_method_button).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_number_field))
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.cvv_field))
        self.driver.find_element(*self.cvv_field).send_keys(card_code)

        self.driver.find_element(*self.cambio_enfoque).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.add_button))
        self.driver.find_element(*self.add_button).click()

        self.driver.find_element(*self.close_button_card).click()

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.cvv_field).get_property('value')

    def write_message_for_driver(self, message):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.message_field))
        self.driver.find_element(*self.message_field).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def order_blanket_tissues(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.blanket_tissue_slider))
        self.driver.find_element(*self.blanket_tissue_slider).click()

    def get_blanket_tissues(self):
        slider = self.driver.find_element(*self.blanket_tissue_slider)
        return slider.is_selected()

    def order_ice_creams(self):
        self.driver.find_element(*self.order_ice_creams_button).click()
        self.driver.find_element(*self.order_ice_creams_button).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_count).text

    def order_taxi(self):
        self.driver.find_element(*self.confirm_taxi).click()

    def wait_driver_information_modal(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.driver_information_modal)
        )

    def get_driver_information_modal(self):
        return self.driver.find_element(*self.driver_information_modal).text
