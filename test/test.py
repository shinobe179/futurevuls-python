import os
import sys
import time
import unittest
from datetime import datetime, timedelta, timezone

import test_data
import test_params

sys.path.append('..')
import futurevuls

UTC = timezone(timedelta(hours=0), 'UTC')
TOKEN = os.environ['FUTUREVULS_TOKEN']


class TestCase(unittest.TestCase):

    def setUp(self):
        self.fv = futurevuls.FutureVulsAPIClient(TOKEN)

    def test_check_health(self):
        self.assertTrue(self.fv.check_health())

    def test_get_cve(self):
        cve_id = 'CVE-2019-20041'
        result = self.fv.get_cve(cve_id)
        self.assertEqual(result['response'], test_data.cve_2019_20041_data)

    def test_get_cves(self):
        pass

    def test_create_paste_server(self):
        body = test_data.paste_server_body
        server_name = 'TestServerForCreatingPasteServer-' + datetime.strftime(datetime.now(UTC), '%Y%m%d-%H%M%S')
        body['serverName'] = server_name
        result = self.fv.create_paste_server(body)
        self.assertEqual(result['response']['serverName'], server_name)

    def test_get_server(self):
        server_name = test_params.server_name
        server_id = test_params.server_id
        result = self.fv.get_server(server_id)
        self.assertEqual(result['response']['serverName'], server_name)

    def test_get_server_uuid(self):
        server_name = test_params.server_name
        server_uuid = test_params.server_uuid
        result = self.fv.get_server_uuid(server_uuid)
        self.assertEqual(result['response']['serverName'], server_name)

    def test_get_servers(self):
        server_name = test_params.server_name
        result = self.fv.get_servers()
        servers = result['response']['servers']
        for srv in servers:
            if srv['serverName'] == server_name:
                self.assertEqual(srv['serverName'], server_name)

    def test_delete_server(self):
        body = test_data.paste_server_body
        server_name = 'TestServerForServerDeletion-' + datetime.strftime(datetime.now(UTC), '%Y%m%d-%H%M%S')
        body['serverName'] = server_name
        _ = self.fv.create_paste_server(body)
        time.sleep(5)

        result = self.fv.get_servers()
        servers = result['response']['servers']
        for srv in servers:
            if srv['serverName'] == server_name:
                result = self.fv.delete_server(srv['id'])
                self.assertTrue(result)

    def tearDown(self):
        result = self.fv.get_servers()
        servers = result['response']['servers']
        for srv in servers:
            if 'TestServer' in srv['serverName']:
                result = self.fv.delete_server(srv['id'])
                print(f'deleted server: {srv["serverName"]}, result: {result}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
