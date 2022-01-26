from logging import Logger
from rpyc.utils.server import ThreadedServer
from .service import Service


class Server:
    """Runs a rpyc ThreadedServer in a seperate process in Background"""

    def __init__(
        self,
        service: Service,
        host: str = "localhost",
        port: int = 18112,
        ipv6: bool = False,
        logger: Logger = None,
    ) -> None:
        self.service = service
        self.host = host
        self.port = port
        self.ipv6 = ipv6
        self.logger = logger
        self._server = None

    @property
    def server(self) -> ThreadedServer:
        return self._server

    def start(self) -> None:
        if self.server is not None:
            self.server = ThreadedServer(
                service=self.service,
                hostname=self.host,
                port=self.port,
                ipv6=self.ipv6,
                logger=self.logger,
            )
            self.server.start()
