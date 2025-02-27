#Standard Library
import time
import logging

#Installed
import requests

#Local
from ._session_types import CWPSession

class CWPSessionManager:
    def __init__(self, tenant_name: str, api_url: str, logger: object, uname='', passwd='', api_token=''):
        """
        Initializes a Prisma Cloud API Session Manager.

        Keyword Arguments:
        tenant_name -- Name of tenant associated with session
        a_key -- Tenant Access Key
        s_key -- Tenant Secret Key
        api_url -- API URL Tenant is hosted on 
        """
        self.logger = logger

        self.tenant = tenant_name
        self.uname = uname
        self.passwd = passwd
        self.api_token = api_token
        self.api_url = api_url

        self.cwp_session = {}        


#==============================================================================
    def create_cwp_session(self):
        session = CWPSession(self.tenant, self.api_url, self.uname, self.passwd, self.logger)
        self.cwp_session = session
        return session
