import portend
import pytest

from . import PostgresServer


@pytest.fixture(scope="session")
def postgresql_instance():
    try:
        port = portend.find_available_local_port()
        instance = PostgresServer(port=port)
        instance.initdb()
        instance.start()
        yield instance
    # Any failure means Postgres is unavailable; only reached where it is absent.
    except Exception as err:  # pragma: no cover  # noqa: BLE001
        pytest.skip(f"Postgres not available ({err})")
    instance.destroy()
