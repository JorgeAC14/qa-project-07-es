Descripción del Proyecto:
El proyecto se centra en automatizar el proceso de pedido de taxi en una aplicación web llamada Urban Routes. Utiliza Selenium WebDriver, una herramienta de automatización de pruebas, para simular las acciones realizadas por un usuario al solicitar un taxi a través de la interfaz web. Esto incluye ingresar la dirección de origen y destino, seleccionar un tipo de taxi y una tarifa, ingresar el número de teléfono, agregar una tarjeta de crédito, escribir un mensaje opcional para el conductor y confirmar el pedido.

Descripción de Tecnologías y Técnicas Utilizadas:
- Selenium WebDriver: Se utiliza para automatizar las interacciones con la interfaz web de la aplicación de transporte urbano.
- Python: El código de automatización está escrito en Python, un lenguaje de programación ampliamente utilizado y compatible con Selenium WebDriver.
- Esperas Explícitas: Se emplean esperas explícitas proporcionadas por la clase 'WebDriverWait' para garantizar que los elementos de la página estén presentes y sean interactuables antes de realizar acciones sobre ellos. Esto mejora la estabilidad y confiabilidad de las pruebas automatizadas.
- Localizadores de Elementos: Se utilizan diferentes métodos de localización de elementos, como ID, CLASS_NAME, CSS_SELECTOR y XPATH, para identificar de manera única los elementos de la interfaz web con los que se interactuará durante la automatización.

Instrucciones para Ejecutar las Pruebas:
1. Asegúrate de tener instalado Python en tu sistema.
2. Instala Pytest para Python ejecutando 'pip install pytest'
3. Instala Selenium WebDriver para Python ejecutando 'pip install selenium' en tu terminal.
4. Descarga el controlador de Selenium WebDriver para el navegador Chrome y asegúrate de que esté en tu PATH o especifica su ubicación en el código.
5. En el archivo data.py, sustituye la url por una nueva que se acabe de generar.
6. Ejecuta el archivo Test_order_taxi.py para iniciar las pruebas automatizadas.
7. Observa la ejecución de las pruebas en el navegador Chrome mientras Selenium simula las acciones del usuario en la aplicación web.
8. Después de que se completen las pruebas, revisa la consola para obtener resultados o errores.

Siguiendo estos pasos, podrás ejecutar las pruebas de forma efectiva y obtener información valiosa sobre el funcionamiento de la aplicación web de Urban Routes.
