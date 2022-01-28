# Aflorithmic Python bindings
# API docs at https://docs.api.audio/

# Configuration variables
sdk_version = "0.13.0"
api_key = None
client_id = None
api_base = "https://v1.api.audio"
upload_api_base = "https://file.api.audio"  # not implemented yet.

# future
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = True
max_network_retries = 0

# API resources
from apiaudio.api_resources import *

# logging
from apiaudio.logging import SDKLogger
APILogger = SDKLogger("apiaudio")
