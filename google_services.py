"""
TODO: Add suitable docstring
"""
import os
from calibre.utils.config import prefs
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# DATA FORM:
# {
#     "client_id":
#     "113366937304-oq2aosgfkg62qd2ile3vd4bpvmdve8if.apps.googleusercontent.com",
#
#     "project_id": "calibre-play-books",
#
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#
#     "token_uri": "https://accounts.google.com/o/oauth2/token",
#
#     "auth_provider_x509_cert_url":
#     "https://www.googleapis.com/oauth2/v1/certs",
#
#     "client_secret": "xxxxxxxxxxxxxxxxxxxx-xxx",
#
#     "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
# }

# TODO: REMOVE BEFORE MAKING PUBLIC
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
credentials = None
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "./client_secret.json"

# This access scope grants read-write access to the authenticated user's Books
# account, and write access to user's Drive account for appdata & files.
BOOKS_API = {'API_SERVICE_NAME': 'books', 'API_VERSION': 'v1'}
DRIVE_API = {'API_SERVICE_NAME': 'drive', 'API_VERSION': 'v3'}
SCOPES = [
    'https://www.googleapis.com/auth/books',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.file']


def get_credentials():
    """
    Gets OAuth 2.0 credentials via the flow's server strategy

    Returns:
        google.oauth2.credentials.Credentials: The user's OAuth 2.0 credentials

    """
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE,
                                                     scopes=SCOPES)
    return flow.run_local_server()

def get_authenticated_service(api):
    """
    Gets authenticated service of an API for its usage

    Args:
        api (dict): Dict with valid key-values for 'API_SERVICE_NAME'
            and 'API_VERSION'. Should be reflected in 'SCOPES'.

    Returns:
        googleapiclient.discovery.build.Resource: Resource object for
            interacting with the passed-in param 'api'.

    """
    if not credentials or credentials.invalid:
        credentials = get_credentials()

    return build(api['API_SERVICE_NAME'],
                 api['API_VERSION'],
                 credentials=credentials)
