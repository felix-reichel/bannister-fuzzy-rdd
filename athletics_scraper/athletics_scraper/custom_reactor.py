import asyncio
from twisted.internet import asyncioreactor


def install_asyncio_reactor():
    try:
        asyncioreactor.install(eventloop=asyncio.get_event_loop())
    except Exception as e:
        print(f"Error installing asyncio reactor: {e}")
