import argparse
from logging import getLogger
import os
import stat
import sys
import time

from CO2Meter import CO2Meter
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY

from co2meter_exporter.collector import CustomCollector


_LOGGER = getLogger(__name__)

parser = argparse.ArgumentParser(
    description='Prometheus exporter for CO2 meter')
parser.add_argument('--device', type=str, required=True,
                    help='device of CO2 meter (example: /dev/hidraw0)')
parser.add_argument('--host', default='0.0.0.0',
                    help='host (default: 0.0.0.0)')
parser.add_argument('--port', type=int, default=9817,
                    help='port number (default: 9817)')
args = parser.parse_args()

device = args.device

if not stat.S_ISCHR(os.lstat(device).st_mode):
    _LOGGER.error("Device is not a character special device: %s", device)
    sys.exit(1)

meter = CO2Meter(device)
REGISTRY.register(CustomCollector(meter))
_LOGGER.info("Using CO2Meter at %s", device)

host = args.host
port = args.port
start_http_server(port, host)
_LOGGER.info("Listening on %s:%d", host, port)
while True:
    time.sleep(1)
