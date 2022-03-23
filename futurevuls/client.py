import logging

import requests

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s - %(funcName)s - %(lineno)d - "%(message)s"')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

URL = 'https://rest.vuls.biz'


class FutureVulsAPIClient:

    def __init__(self, token, debug=False):
        self.set_token(token)
        if debug is True:
            logger.setLevel(logging.DEBUG)

    def set_token(self, token):
        """Set API token.

        Parameters
        ----------------
        token : str
            API token.

        Returns
        -----------
        none
        """
        self.headers = {'Authorization': token}

    def check_health(self):
        """Check health of https://vuls.biz.

        Parameters
        ----------------
        none

        Returns
        -----------
        result : dict
            Status code and response body.
        """

        resp = requests.get(URL + '/health')
        logger.debug('status_code: %s, response_body: %s', resp.status_code, resp.json())
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def get_cve(self, cve_id):
        """
        Get specified CVE information.

        Paramaters
        ----------------
        cve_id : str
            CVE ID you wont to get.

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        resp = requests.get(URL + f'/v1/cve/{cve_id}', headers=self.headers)
        logger.debug('cve_id: %s, status_code, %s, response_body: %s', cve_id, resp.status_code, resp)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def get_cves(
        self,
        page=None,
        limit=None,
        offset=None,
        filter_server_id=None,
        filter_role_id=None,
        filter_pkg_id=None,
        filter_cpe_id=None
    ):
        """
        Get  CVE informations through specified filters.

        Paramaters
        ----------------
        page : int
        limit : int
        offset : int
        filter_server_id : int
        filter_role_id : int
        filter_pkg_id : int
        filter_cpe_id : int

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        params = {
           'page': page,
           'limit': limit,
           'offset': offset,
           'filterServerID': filter_server_id,
           'filterRoleID': filter_role_id,
           'filterPkgID': filter_pkg_id,
           'filterCpeID': filter_cpe_id
        }

        resp = requests.get(URL + '/v1/cves', headers=self.headers, params=params)
        logger.debug('params: %s, status_code, %s, response_body: %s', params, resp.status_code, resp)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def create_paste_server(self, body):
        """
        Create pasete server.

        Parameters
        ----------------
        body : dict
            Information for creating paste server.

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        resp = requests.post(URL + '/v1/server/paste', headers=self.headers, json=body)
        logger.debug('cve_id: %s, status_code, %s, response_body: %s', body, resp.status_code, resp)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def get_server_uuid(self, server_uuid):
        """
        Get specified serverinformation by server UUID.

        Paramaters
        ----------------
        server_uuid : str
            Server ID you wont to get.

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        resp = requests.get(URL + f'/v1/server/uuid/{server_uuid}', headers=self.headers)
        logger.debug('server_uuid: %s, status_code: %s, response_body: %s', server_uuid, resp.status_code, resp)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def get_server(self, server_id):
        """
        Get specified serverinformation.

        Paramaters
        ----------------
        server_id : str
            Server ID you wont to get.

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        resp = requests.get(URL + f'/v1/server/{server_id}', headers=self.headers)
        logger.debug('server_id: %s, status_code: %s, response_body: %s', server_id, resp.status_code, resp)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def delete_server(self, server_id):
        """
        Delete specified serverinformation.

        Paramaters
        ----------------
        server_id : str
            Server ID you wont to delete.

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        resp = requests.delete(URL + f'/v1/server/{server_id}', headers=self.headers)
        logger.debug('server_id: %s, status_code: %s', server_id, resp.status_code)
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result

    def get_servers(
        self,
        page=None,
        limit=None,
        offset=None,
        filter_cve_id=None,
        filter_role_id=None,
    ):
        """
        Get  server informations through specified filters.

        Paramaters
        ----------------
        page : int
        limit : int
        offset : int
        filter_cve_id : int
        filter_role_id : int

        Returns
        -----------
        result : dict
            Status code and response body.
        """
        params = {
           'page': page,
           'limit': limit,
           'offset': offset,
           'filterCveID': filter_cve_id,
           'filterRoleID': filter_role_id
        }

        resp = requests.get(URL + '/v1/servers', headers=self.headers, params=params)
        logger.debug('params: %s, status_code: %s, response_body: %s', params, resp.status_code, resp.json())
        result = {'status_code': resp.status_code, 'response_body': resp.json()}

        return result
