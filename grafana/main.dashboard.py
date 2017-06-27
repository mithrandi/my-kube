import grafanalib.core as G

dashboard = G.Dashboard(
    title='UCDAPI',
    rows=[
        G.Row(panels=[
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
                        legendFormat='{{pod}} 0.9 q',
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
                        legendFormat='{{pod}} 0.99 q',
                        refId='A',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                ]),
        ]),
    ]).auto_panel_ids()
