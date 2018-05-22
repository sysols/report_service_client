import collections

import requests

from .url_resolver import ReportServiceURLResolver


RenderedFileInfo = collections.namedtuple(
    'RenderedFileInfo',
    (
        'file_url',
    )
)


class ReportServiceClient(object):
    def __init__(self, url_resolver: ReportServiceURLResolver=None):
        self.url_resolver = url_resolver or ReportServiceURLResolver()

    def render_file_report(self, report_file_slug: str, context: dict) -> RenderedFileInfo:
        response_json = self._render(
            self.url_resolver.get_url_for_render(report_file_slug=report_file_slug),
            context=context,
        )
        rendered_file_id = response_json['id']

        return RenderedFileInfo(
            file_url=self.url_resolver.get_url_for_document(file_id=rendered_file_id)
        )

    def _render(self, api_url: str, context: dict) -> dict:
        response = requests.post(api_url, json=context)

        if response.status_code != 201:
            raise ConnectionError(response.text)

        response_json = response.json()
        error_messages = response_json.get('error', None)
        if error_messages is not None:
            raise ConnectionError(error_messages)

        return response_json
