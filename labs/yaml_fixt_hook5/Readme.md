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


