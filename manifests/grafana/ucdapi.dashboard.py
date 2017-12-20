import grafanalib.core as G

YELLOW = "#EAB839"
GREEN = "#7EB26D"
BLUE = "#6ED0E0"
ORANGE = "#EF843C"
RED = "#E24D42"

ALIAS_COLORS = {
  "1xx": YELLOW,
  "2xx": GREEN,
  "3xx": BLUE,
  "4xx": ORANGE,
  "5xx": RED,
  "success": GREEN,
  "error": RED,
}

dashboard = G.Dashboard(
    title='UCDAPI',
    rows=[
        G.Row(panels=[
            G.SingleStat(
                title='Pods Up',
                dataSource='prometheus',
                valueName='current',
                sparkline=G.SparkLine(show=True),
                targets=[
                    G.Target(
                        expr='count by(service) (up{service="ucdapi"} == 1)',
                    )]),
        ]),
        G.Row(panels=[
            G.Graph(
                title='HTTP RPS',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='service_status:http_request_duration_seconds_count:irate{service="ucdapi",status_code=~"1.."}',
                        legendFormat='1xx',
                        refId='A'),
                    G.Target(
                        expr='service_status:http_request_duration_seconds_count:irate{service="ucdapi",status_code=~"2.."}',
                        legendFormat='2xx',
                        refId='B'),
                    G.Target(
                        expr='service_status:http_request_duration_seconds_count:irate{service="ucdapi",status_code=~"3.."}',
                        legendFormat='3xx',
                        refId='C'),
                    G.Target(
                        expr='service_status:http_request_duration_seconds_count:irate{service="ucdapi",status_code=~"4.."}',
                        legendFormat='4xx',
                        refId='D'),
                    G.Target(
                        expr='service_status:http_request_duration_seconds_count:irate{service="ucdapi",status_code=~"5.."}',
                        legendFormat='5xx',
                        refId='E'),
                ],
                aliasColors=ALIAS_COLORS,
                yAxes=[G.YAxis(format=G.OPS_FORMAT),
                       G.YAxis(format=G.SHORT_FORMAT, show=False)],
                nullPointMode=G.NULL_AS_ZERO,
                stack=True,
                lineWidth=0,
                fill=10,
                tooltip=G.Tooltip(valueType=G.INDIVIDUAL)),
            G.Graph(
                title='RPS',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="ucdapi"}[1m])) by (status_code, method)',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.OPS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT),
                ]),
        ]),
        G.Row(panels=[
            G.Graph(
                title='Latency 0.9q',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='http_request_duration_seconds{quantile="0.9",status_code="200",service="ucdapi"}*1000',
                        legendFormat='{{pod}}',
                        refId='A',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                ]),
            G.Graph(
                title='Latency 0.99q',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='http_request_duration_seconds{quantile="0.99",status_code="200",service="ucdapi"}*1000',
                        legendFormat='{{pod}}',
                        refId='A',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                ]),
        ]),
    ]).auto_panel_ids()
