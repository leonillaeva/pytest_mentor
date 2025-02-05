import pytest
from selenium import webdriver
from labs.loging.creds import USER_AGENT


# 1
# # @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# def driver(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

# 2
@pytest.fixture(scope="class")
def driver(request):

    options = webdriver.ChromeOptions()
    # options.add_argument('dom.webdriver.enabled', False)
    options.add_argument(f"--user-agent={USER_AGENT}")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def driver_headless(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # New headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=VizDisplayCompositor")  # Disable VizDisplayCompositor

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  # Set the driver as a class attribute
    yield
    driver.quit()


def pytest_runtest_makereport(item, call):
    """Этот хук используется для захвата дополнительной информации (в данном случае снимков экрана)
    в случае, если тест падает. Она обрабатывает состояние теста после каждого вызова (call) и выполняет действие,
    если тест завершился с ошибкой.
    Проверяет, был ли тест завершен с ошибкой (call.excinfo is not None).
    Доступ к фикстурам теста осуществляется через item.funcargs.
    Если драйвер Selenium доступен, создается скриншот текущего экрана, который можно использовать для отладки.

"""
    if call.when == "call" and call.excinfo is not None:
        # Снимок экрана при ошибке
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")


def pytest_sessionstart(session):
    """Пример: Логирование начала тестовой сессии.
    Вызывается один раз перед началом всей сессии тестов.
    Применение: Инициализация глобальных переменных, подключение к базе данных, логирование начала тестовой сессии."""
    print("Начало тестовой сессии. Тесты начаты!")


def pytest_sessionfinish(session, exitstatus):
    """ Пример: Генерация общего отчета или закрытие внешних ресурсов.
    Вызывается один раз после завершения всей сессии тестов.
    Применение: Закрытие соединений, выгрузка отчетов, очистка ресурсов."""
    print(f"Тестовая сессия завершена с кодом {exitstatus}")


def pytest_runtest_setup(item):
    """Пример: Убедиться, что драйвер Selenium инициализирован и открыта нужная страница перед каждым тестом.
    Вызывается перед каждым тестом, перед его выполнением.
    Применение: Подготовка окружения для теста, например, очистка данных, проверка доступности ресурсов."""
    print(f"Подготовка к тесту {item.name}")
    driver = item.funcargs.get("driver")
    if driver and "https://example-courses-site.com" not in driver.current_url:
        driver.get("https://example-courses-site.com")


def pytest_runtest_teardown(item):
    """ Пример: Очистка cookies после каждого теста для предотвращения перекрестного влияния.
    Вызывается после выполнения теста.
    Применение: Очистка после теста, например, удаление временных данных или файлов."""
    print(f"Завершение теста {item.name}")
    driver = item.funcargs.get("driver")
    if driver:
        driver.delete_all_cookies()
