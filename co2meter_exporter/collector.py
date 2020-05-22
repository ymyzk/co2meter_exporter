from typing import Dict, Generator

from CO2Meter import CO2Meter
from prometheus_client.core import GaugeMetricFamily


_METRICS = {
    "co2": "CO2 in ppm",
    "temperature": "Temperature in degrees Celsius",
    "humidity": "Relative humidity %",
}


class CustomCollector:
    def __init__(self, meter: CO2Meter) -> None:
        self.meter = meter

    def _make_gauge_metric(
        self, data: Dict[str, float], field: str, description: str
    ) -> GaugeMetricFamily:
        if field not in data:
            return None

        g = GaugeMetricFamily("co2meter_" + field, description, labels=["device"])
        g.add_metric([self.meter._device], data[field])
        return g

    def collect(self) -> Generator[GaugeMetricFamily, None, None]:
        # TODO: We may want to reinitialize the meter or exit the application
        #       when the meter is unhealthy
        data = self.meter.get_data()
        for field, description in _METRICS.items():
            gauge = self._make_gauge_metric(data, field, description)
            if gauge is None:
                continue
            yield gauge
