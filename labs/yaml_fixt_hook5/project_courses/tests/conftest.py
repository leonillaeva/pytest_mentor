import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://example-courses-site.com")
    yield driver
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


def pytest_collection_modifyitems(session, config, items):
    """ Пример: Автоматически помечать тесты с определенными словами в имени как skip.
    Используется для модификации списка тестов перед их выполнением.
    Применение: Фильтрация, переупорядочивание тестов, добавление меток."""
    for item in items:
        if "skip" in item.nodeid:
            item.add_marker(pytest.mark.skip(reason="Пропущенный тест"))
        if "not_valid" in item.name:
            item.add_marker(pytest.mark.skip(reason="Пропущен: негативный сценарий"))


def pytest_addoption(parser):
    """Позволяет добавлять пользовательские параметры командной строки.
    Применение: Добавление аргументов для тестов, например, --browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")


def pytest_configure(config):
    """Позволяет изменять глобальную конфигурацию Pytest.
    Применение: Настройка логов, добавление глобальных плагинов."""
    config.option.maxfail = 3  # Завершать сессию после 3 ошибок



