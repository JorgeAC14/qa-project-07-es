import data
from selenium import webdriver
import Urban_Routes_Page


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

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)

        # Configurar dirección
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_taxi(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Seleccionar taxi
        routes_page.select_taxi()
        assert routes_page.comfort_tariff_button is not None, "No se pudo pedir el taxi"

    def test_select_comfort(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        assert routes_page.blanket_tissue_slider is not None, "No se pudo seleccionar tarifa comfort"

    def test_phone_number(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Seleccionar campo número de telefono
        routes_page.click_phone_number()
        # Rellenar número de teléfono
        routes_page.fill_phone_number(data.phone_number)
        routes_page.fill_sms_code()
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_credit_card(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Agregar tarjeta de crédito
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert routes_page.get_card_number() == data.card_number
        assert routes_page.get_card_code() == data.card_code

    def test_write_message(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Escribir mensaje para el conductor
        routes_page.write_message_for_driver(data.message_for_driver)
        assert routes_page.get_message() == data.message_for_driver

    def test_blanket_tissue(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Pedir una manta y pañuelos
        routes_page.order_blanket_tissues()
        assert routes_page.get_blanket_tissues() is not None, "No se pudo pedir la manta y pañuelos"

    def test_order_ice_creams(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Pedir 2 helados
        routes_page.order_ice_creams()
        assert routes_page.get_ice_cream_count() == '2'

    def test_confirm_taxi(self):
        routes_page = Urban_Routes_Page.UrbanRoutesPage(self.driver)
        # Confiramar taxi
        routes_page.order_taxi()
        # Aparece el modal para buscar un taxi
        # Esperar a que aparezca la información del conductor en el modal
        routes_page.wait_driver_information_modal()
        assert routes_page.get_driver_information_modal() is not None, "No se pudo pedir el taxi"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
