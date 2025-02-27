#Standard Library
import enum

#Installed
import requests

#Local
from ._session_base import Session

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CWPSession(Session):
    def __init__(self, tenant_name: str, api_url: str, uname: str, passwd:str, logger: object):
        """
        Initializes a Prisma Cloud API session for a given tenant.

        Keyword Arguments:
        tenant_name -- Name of tenant associated with session
        api_url -- API URL Tenant is hosted on
        uname -- Username
        passwd -- Password
        token -- Dedicated API token
        """

        super().__init__(logger)

        self.tenant = tenant_name
        self.uname = uname
        self.passwd = passwd

        self.api_url = api_url

        self.logger = logger

        self.auth_key = 'Authorization'
        self.auth_style = 'Bearer '

        self.headers = {
            'content-type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer '
        }

        self._api_login_wrapper()

#==============================================================================
    def _api_login(self) -> object:
        '''
        Calls the Prisma Cloud API to generate a x-redlock-auth JWT.

        Returns:
        x-redlock-auth JWT.
        '''

        #Build request
        url = f'{self.api_url}/api/v1/authenticate'
        
        headers = {
            'content-type': 'application/json; charset=UTF-8'
            }

        payload = {
            "username": self.uname,
            "password": self.passwd,
        }

        self.logger.debug('API - Generating CWP session token.')

        res = object()
        try:
            res = requests.request("POST", url, headers=headers, json=payload)
        except:
            self.logger.error('Failed to connect to API.')
            self.logger.warning('Make sure any offending VPNs are disabled.')
            self.logger.info('Exiting...')
            quit()

        return res

    def _expired_login(self) -> None:
        self.logger.error('FAILED')
        self.logger.warning('Invalid Login Credentials. JWT not generated. Exiting...')
        exit()