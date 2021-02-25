# Aflorithmic Python bindings
# API docs at https://docs.api.audio/
# Authors:
# Antonio Tripiana <antonio@aflorithmic.ai>

# Configuration variables

api_key = None
client_id = None
api_base = "https://api.aflr.io"
upload_api_base = "https://files.aflr.io" # not implemented yet.

# future
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = True
max_network_retries = 0

# Set to either 'debug' or 'info', controls console logging
log = None

# API resources
from aflr.api_resources import *