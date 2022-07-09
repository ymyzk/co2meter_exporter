# co2meter_exporter
## Getting started
1. Follow [heinemml/CO2Meter](https://github.com/heinemml/CO2Meter) to configure udev rules on Linux.
   Other OSs are not tested.
2. Install co2meter_exporter: `pip install git+https://github.com/ymyzk/co2meter_exporter.git`
3. Run co2meter_exporter: `python3 -m co2meter_exporter --device /dev/<your device>`

## Docker
A Docker image is also provided: `docker run --rm -p 9817:9817 --device=/dev/<device> ghcr.io/ymyzk/co2meter_exporter:latest --device /dev/<device>`

## Help
Run `python3 -m co2meter_exporter -h`.
