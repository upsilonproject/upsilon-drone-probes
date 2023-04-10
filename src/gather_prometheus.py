#!/usr/bin/python

from upsilon.service import ServiceController
from configargparse import ArgParser
from prometheus_api_client import PrometheusConnect

parser = ArgParser()
parser.add_argument("-s", "--server", env_var='PROMETHEUS_SERVER', default='http://localhost')
parser.add_argument("-m", "--metrics", env_var='PROMETHEUS_METRIC', default=[], nargs="+")
args = parser.parse_args();

srv = ServiceController();

promcon = PrometheusConnect(url=args.server, disable_ssl=True)

for metricName in args.metrics:
    metricValue = promcon.get_current_metric_value(metric_name=metricName)

    if len(metricValue) == 0:
        srv.addMessageWarning("NotFound: %s" % (metricName))
        continue

    metricValue = metricValue[0]['value'][1]

    srv.addMetric(metricName, metricValue)

srv.exit()
