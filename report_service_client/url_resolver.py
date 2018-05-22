from urllib.parse import urljoin


class ReportServiceURLResolver(object):
    API_URL = 'http://reports.sysols.ru/api/'

    TEMPLATE_URL_SUFFIX = 'template/'
    DOCUMENT_URL_SUFFIX = 'document/'

    def __init__(self, api_url: str=None):
        self.API_URL = api_url or self.API_URL

    def get_template_api_url(self) -> str:
        return urljoin(
            self.API_URL, self.TEMPLATE_URL_SUFFIX
        )

    def get_document_api_url(self) -> str:
        return urljoin(
            self.API_URL, self.DOCUMENT_URL_SUFFIX
        )

    def get_url_for_render(self, report_file_slug: str) -> str:
        return urljoin(
            self.get_template_api_url(), report_file_slug
        )

    def get_url_for_document(self, file_id: str) -> str:
        return urljoin(
            self.get_document_api_url(), file_id
        )
