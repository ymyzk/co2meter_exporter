import argparse
import time

from CO2Meter import CO2Meter
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY

from co2meter_exporter.collector import CustomCollector


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
meter = CO2Meter(device)
REGISTRY.register(CustomCollector(meter))
print("Using CO2Meter at %s" % device)

host = args.host
port = args.port
start_http_server(port, host)
print("Listening on %s:%d" % (host, port))
while True:
    time.sleep(1)
