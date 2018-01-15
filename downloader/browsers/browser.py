import abc


class Browser(abc.ABC):
    def __init__(self):
        self._headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

    def get_headers(self) -> dict:
        self._headers['User-Agent'] = self._get_user_agent()
        return self._headers

    @abc.abstractmethod
    def _get_user_agent(self) -> str:
        pass
