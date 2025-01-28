# YAML
## [YAML Tutorial: Everything You Need to Get Started in Minutes](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)

[The Official YAML WebSite](https://yaml.org/)

[habr. ужасы PyYAML](https://habr.com/ru/articles/669684/)

YAML Ain't Markup Language (YAML) is **_a data serialization language_** that is consistently listed as one of the most popular programming languages.

It's often used as **_a format for configuration files_**, but its object serialization abilities make it a viable replacement for languages like JSON.

The YAML acronym was shorthand for Yet Another Markup Language. 

But the maintainers renamed it to YAML Ain't Markup Language to place more emphasis on its data-oriented features.

(book) Как и JSON? YAML имеет ключи и значения, но обрабатывает большее количество типов данных, включая дату и время. - Простой Python. Билл Любанович. Гл.16, стр. 337
<hr>

**!!!** Всегда должны использовать ***yaml.safe_load и yaml.safe_dump*** в качестве стандартных методов ввода/вывода для YAML**

[loading yaml](https://pyyaml.org/wiki/PyYAMLDocumentation#loading-yaml)

<hr>


| Syntax/format       | Description                                                                                                                                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| indent              | The indentation level can be one or more spaces.                                                                                                                                                                          |
| PyYAML              | pip install pyyaml                                                                                                                                                                                                        |
| oyaml               | oyaml - это замена PyYAML, которая сохраняет упорядочивание словарей. Используйте oyaml, если Вы уже используете PyYAML в своем коде.                                                                                     |
| .yml, .yaml         | format of files                                                                                                                                                                                                           |
| ---                 | start of a file. [A document starts with three dashes and ends with three periods.](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started#multiple-documents)                                      |
| .load()             | преобразует строку в формате YAML к данным Python. Опасно загружать документ при помощи yaml.load из ненадежного источника                                                                                                |
| .safe_load()        | всегда yaml.safe_load                                                                                                                                                                                                     |
| .dump()             | предназначена для противоположного - из данных Python в строку Yaml                                                                                                                                                       |
| .safe_dump()        | безопасная десерилизация                                                                                                                                                                                                  |
| bar: >              | single quotes do avoid having string contents interpreted as document formatting. String values can span more than one line. With the fold (greater than) character, you can specify a string in a block. \n - in the end |
| bar: \|             | The block (pipe) character interprets the field exactly as is - string it\nspans more than\none line\nsee?\n                                                                                                              |
| null, ~             | none                                                                                                                                                                                                                      |
| bar: >+             | strip chomp and preserve chomp operators, no \n sign in the end                                                                                                                                                           |
| strip_operator: \|- | lines will be preserved like a new line without \n sign                                                                                                                                                                   |

# [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

**fixtures** - перевод: _приспособление, зажимное приспособление, заранее назначенный день_

Фикстура в pytest - это функция, которая предоставляет фиксированный ресурс или контекст для тестов. Фикстуры используются для подготовки данных, настройки окружения и выполнения повторяющихся действий до выполнения тестов. 

## “Requesting” fixtures
1. basic level - arguments, pytest passes those objects into the test function as arguments.
2. fixtures request other fixtures - boiling down complex requirements for tests into more simple and organized functions
3. fixtures are reusable - ability to define a generic setup step that can be reused over and over, 
each test has its own result from that fixture. 
Tests aren’t affected by each other
4. request many fixtures - Tests and fixtures aren’t limited to requesting a single fixture at a time. 
They can request as many as they like.
5. requested more than once per test - 
## Others
1. autouse fixtures - fixtures you don’t have to request, way to make all tests automatically request them
2. Scope:
   - Fixture scopes - sharing fixtures across classes, modules, packages or session. Default scope - function
   - Dynamic scope -useful when dealing with fixtures that need time for setup, like spawning a **_docker_** container.
3. Teardown/Cleanup (AKA Fixture finalization):
   - yield fixtures (recommended) - yield instead of return
   - Adding finalizers - It brings a similar result as yield fixtures, but requires a bit more verbosity (подробностей).
   **_request.addfinalizer()_**
4. Safe teardowns
5. Running multiple assert statements safely - run multiple asserts after doing all that setup, which makes sense as, in more complex systems, a single action can kick off multiple behaviors
6. Fixtures can introspect the requesting test context - Fixture functions can accept the request object to introspect the “requesting” test function, class or module context.
7. Using markers to pass data to fixtures - Using the request object, a fixture can also access markers which are applied to a test function. This can be useful to pass data into a fixture from a test

   ***@pytest.mark.fixt_data(42)***
8. Factories as fixtures - The “factory as fixture” pattern can help in situations where the result of a fixture is needed multiple times in a single test. Instead of returning data directly, the fixture instead returns a function which generates the data. 
This function can then be called multiple times in the test
9. Parametrizing fixtures - Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i.e. the tests that depend on this fixture.

   ***@pytest.fixture(scope="module", params=\["smtp.gmail.com", "mail.python.org"])***
10. Using marks with parametrized fixtures - pytest.param() can be used to apply marks in values sets of parametrized fixtures in the same way that they can be used with @pytest.mark.parametrize.

   ***@pytest.fixture(params=\[0, 1, pytest.param(2, marks=pytest.mark.skip)])***
11. Modularity: using fixtures from a fixture function - This contributes to a modular design of your fixtures and allows reuse of framework-specific fixtures across many projects.
12. Automatic grouping of tests by fixture instances - pytest minimizes the number of active fixtures during test runs. If you have a parametrized fixture, then all the tests using it will first execute with one instance and then finalizers are called before the next fixture instance is created.
13. Use fixtures in classes and modules with usefixtures - Sometimes test functions do not directly need access to a fixture object.

   ***@pytest.mark.usefixtures("cleandir")***
14. Overriding fixtures on various levels:
    - Override a fixture on a folder (conftest) level
    - Override a fixture on a test module level
    - Override a fixture with direct test parametrization
    - Override a parametrized fixture with non-parametrized one and vice versa
15. Using fixtures from other projects

## hook
[Расширяем тестовый фреймворк с помощью Pytest-плагинов.](https://habr.com/ru/companies/yadro/articles/789756/)
