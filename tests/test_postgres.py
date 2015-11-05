import os
from unittest import TestCase

import portend
from jaraco.postgres import PostgresDatabase, PostgresServer


HOST = os.environ.get('HOST', 'localhost')


class PostgresServerTest(TestCase):
    def test_serves_postgres(self):
        port = portend.find_available_local_port()
        server = PostgresServer(HOST, port)
        server.initdb()

        try:
            server.start()
            version = server.get_version()

            self.assertGreater(len(version), 0)
            self.assertGreaterEqual(version[0], 8)
        finally:
            server.destroy()


class PostgresDatabaseTest(TestCase):
    def setUp(self):
        self.port = portend.find_available_local_port()
        self.server = PostgresServer(HOST, self.port)
        self.server.initdb()
        self.server.start()

    def tearDown(self):
        self.server.destroy()

    def test_creates_user_and_database(self):
        database = PostgresDatabase(
            'tests', user='john', host=HOST, port=self.port)

        database.create_user()
        database.create()

        rows = database.sql('SELECT 1')

        self.assertEqual(rows, [(1, )])
