
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


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
    close_button_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    # Mensaje
    message_field = (By.ID, 'comment')

    # Pedir manta y pañuelos
    blanket_tissue_slider = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")

    # Pedir helado
    order_ice_creams_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")

    # Pedir taxi
    confirm_taxi = (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button")

    # Información del conductor en el modal
    driver_information_modal = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

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

    def fill_sms_code(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.sms_code_field))
        self.driver.find_element(*self.sms_code_field).send_keys(retrieve_phone_code(self.driver))
        self.driver.find_element(*self.sms_confirm_button).click()

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

    def write_message_for_driver(self, message):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.message_field))
        self.driver.find_element(*self.message_field).send_keys(message)

    def order_blanket_tissues(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.blanket_tissue_slider))
        self.driver.find_element(*self.blanket_tissue_slider).click()

    def order_ice_creams(self):
        self.driver.find_element(*self.order_ice_creams_button).click()
        self.driver.find_element(*self.order_ice_creams_button).click()


    def order_taxi(self):
        self.driver.find_element(*self.confirm_taxi).click()

    def wait_for_driver_information_modal(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.driver_information_modal)
        )


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de
        # confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_full_taxi_order_process(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Configurar dirección
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)

        # Seleccionar taxi
        routes_page.select_taxi()
        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()

        # Seleccionar campo número de telefono
        routes_page.click_phone_number()

        # Rellenar número de teléfono
        routes_page.fill_phone_number(data.phone_number)

        # Agregar codigo sms
        routes_page.fill_sms_code()

        # Agregar tarjeta de crédito
        routes_page.add_credit_card(data.card_number, data.card_code)

        # Escribir mensaje para el conductor
        routes_page.write_message_for_driver(data.message_for_driver)

        # Pedir una manta y pañuelos
        routes_page.order_blanket_tissues()

        # Pedir 2 helados
        routes_page.order_ice_creams()

        # Confiramr taxi
        routes_page.order_taxi()

        # Aparece el modal para buscar un taxi

        # Esperar a que aparezca la información del conductor en el modal
        routes_page.wait_for_driver_information_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
