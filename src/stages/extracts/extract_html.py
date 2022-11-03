from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface

class ExtractHtml:
    def __init__(self, http_requester: HttpRequesterInterface, html_collector: HtmlCollectorInterface) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self):
        html_information = self.__http_requester.request_from_page()
        essencial_information = self.__html_collector.collect_essencial_information(html_information["html"])
        return essencial_information
