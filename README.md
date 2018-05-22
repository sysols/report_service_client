# Клиент сервиса построения отчетов

## Пример использования
```python
from report_service_client import ReportServiceClient

rs_client = ReportServiceClient()
file_info = rs_client.render_file_report(
    report_file_slug=report_file_slug, context=context
)
print(file_info.file_url)

```


Метод **render_file_report** объекта класс **ReportServiceClient** возвращает структуру типа
**RenderedFileInfo**. Структура содержит следующие поля:
* file_url - URL для скачивания сформированного файла;

**ВАЖНО!** Если в процессе работы метода **render_file_report**  возникли ошибки, то будет вызвано исключение
ConnectionError с описанием ошибки.

## Возможность настройки
В конструктор класса **ReportServiceClient** в качестве аргумента можно передать **url_resolver**.
Переданный объект должен обязательно реализовывать следующие методы:
* get_url_for_render(self, report_file_slug: str) -> str
* get_url_for_document(self, file_id: str) -> str


**ВАЖНО!** По умолчанию в качестве **url_resolver** принимается объект класса **ReportServiceURLResolver**.
Конструктор данного класса принимает необязательный аргумент **api_url**.