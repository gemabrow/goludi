"""
TODO: Add suitable docstring
"""
import os
#from calibre.utils.config import prefs
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


class GoogleServices():
    """ Class for accessing Google APIs.
    """
    # TODO: REMOVE BEFORE MAKING PUBLIC
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # The CLIENT_SECRETS_FILE variable specifies the name of a file that
    # contains the OAuth 2.0 information for this application, including its
    # client_id and client_secret.
    CLIENT_SECRETS_FILE = "./client_secret.json"

    # This access scope grants read-write access to the user's Books account,
    # and write access to the user's Drive account for appdata & files.
    BOOKS_API = {'API_SERVICE_NAME': 'books',
                 'API_VERSION': 'v1',
                 'SCOPES': ['https://www.googleapis.com/auth/books']}
    DRIVE_API = {'API_SERVICE_NAME': 'drive',
                 'API_VERSION': 'v3',
                 'SCOPES': ['https://www.googleapis.com/auth/drive.appdata',
                            'https://www.googleapis.com/auth/drive.file']}
    DEFAULT_SERVICES = [BOOKS_API, DRIVE_API]

    def __init__(self):
        # TODO: fetch pre-existing credentials
        self.services = dict()
        self.credentials = None

        # get the set of all scopes from all services
        self.all_scopes = {scope for service in self.DEFAULT_SERVICES
                           for scope in service['SCOPES']}

        self.authenticate_services(self.DEFAULT_SERVICES,
                                   self.CLIENT_SECRETS_FILE)

    def authenticate_services(self, services, client_secrets_file):
        """Authenticate each service in services.

        Args:
            services (:obj:`list` of :obj:`dict`): A list of dictionaries.
                Each dictionary represents a Google service with API access,
                supported by the client secret, and includes corresponding
                key-values as exampled below.
            client_secrets_file (str): Path to a client_secrets.json file.

        Examples:
            The form of each dictionary representing a service in `services`.

            >>> print(services[1])
            {'API_SERVICE_NAME': 'drive', 'API_VERSION': 'v3',
            'SCOPES': ['https://www.googleapis.com/auth/drive.appdata',
            'https://www.googleapis.com/auth/drive.file']}

        """
        for service in services:
            service['API'] = self.get_authenticated_service(
                service, client_secrets_file)

            service_name = service['API_SERVICE_NAME']
            self.services[service_name] = service

    def get_authenticated_service(self, service, client_secrets_file):
        """Authenticate an API service and return a Resource for its usage.

        Args:
            service (:obj:`dict`): A dictionary for a service. Represents a
                Google service with API access supported by the client secret.
            client_secrets_file (str): Path to a client_secrets.json file.

        Returns:
            googleapiclient.discovery.build.Resource: Resource object for
                interacting with a Google API service

        """
        if not self.credentials or self.credentials.invalid:
            self.credentials = self.get_credentials(client_secrets_file)

        return build(service['API_SERVICE_NAME'],
                     service['API_VERSION'],
                     credentials=self.credentials)

    def get_credentials(self, client_secrets_file):
        """Get OAuth 2.0 credentials via the flow server strategy

        Args:
            client_secrets_file (str): Path to a client_secrets.json file.

        Returns:
            google.oauth2.credentials.Credentials: The user's OAuth 2.0
                credentials for the scopes in `self.all_scopes`

        """
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file,
            scopes=list(self.all_scopes))

        return flow.run_local_server()
