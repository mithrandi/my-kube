import grafanalib.core as G

dashboard = G.Dashboard(
    title=u'UCDAPI',
    rows=[
        G.Row(panels=[
            G.Graph(
                title=u'RPS',
                dataSource=u'prometheus',
                targets=[
                    G.Target(
                        expr=u'sum(irate(http_request_duration_seconds_count{service="ucdapi"}[1m])) by (status_code, method)',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.OPS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT),
                ]),
            G.Graph(
                title=u'Latency',
                dataSource=u'prometheus',
                targets=[
                    G.Target(
                        expr=u'http_request_duration_seconds{quantile="0.9",status_code="200",service="ucdapi"}*1000',
                        legendFormat=u'{{pod}} 0.9 q',
                    ),
                    G.Target(
                        expr=u'http_request_duration_seconds{quantile="0.99",status_code="200",service="ucdapi"}*1000',
                        legendFormat=u'{{pod}} 0.99 q',
                    ),
                ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                ]),
        ]),
    ]).auto_panel_ids()
