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

def make(prefix, title):
    def target(expr, **kw):
        return G.Target(expr=expr.format(prefix), **kw)
    return G.Dashboard(
        title=title,
        rows=[
            G.Row(panels=[
                G.SingleStat(
                    title='Pods up (web)',
                    dataSource='prometheus',
                    valueName='current',
                    sparkline=G.SparkLine(show=True),
                    targets=[target(expr='count by(service) (up{{service="{}-isaacranks"}} == 1)')]),
                G.SingleStat(
                    title='Pods up (rebuild)',
                    dataSource='prometheus',
                    valueName='current',
                    sparkline=G.SparkLine(show=True),
                    targets=[target(expr='count by(service) (up{{service="{}-rebuild"}} == 1)')]),
            ]),
            G.Row(panels=[
                G.Graph(
                    title='HTTP RPS',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='sum(irate(http_request_duration_seconds_count{{service="{}-isaacranks",status_code=~"1.."}}[5m]))',
                            legendFormat='1xx',
                            refId='A'),
                        target(
                            expr='sum(irate(http_request_duration_seconds_count{{service="{}-isaacranks",status_code=~"2.."}}[5m]))',
                            legendFormat='2xx',
                            refId='B'),
                        target(
                            expr='sum(irate(http_request_duration_seconds_count{{service="{}-isaacranks",status_code=~"3.."}}[5m]))',
                            legendFormat='3xx',
                            refId='C'),
                        target(
                            expr='sum(irate(http_request_duration_seconds_count{{service="{}-isaacranks",status_code=~"4.."}}[5m]))',
                            legendFormat='4xx',
                            refId='D'),
                        target(
                            expr='sum(irate(http_request_duration_seconds_count{{service="{}-isaacranks",status_code=~"5.."}}[5m]))',
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
                    title='HTTP latency',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='histogram_quantile(0.5, sum(irate(http_request_duration_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.5q',
                            refId='A'),
                        target(
                            expr='histogram_quantile(0.9, sum(irate(http_request_duration_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.9q',
                            refId='B'),
                        target(
                            expr='histogram_quantile(0.99, sum(irate(http_request_duration_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.99q',
                            refId='C'),
                    ],
                    aliasColors=ALIAS_COLORS,
                    yAxes=[G.YAxis(format=G.MILLISECONDS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)]),
            ]),
            G.Row(panels=[
                G.Graph(
                    title='Ballots',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='sum(irate(isaacranks_ballot_generation_seconds_count[5m])) by (version)',
                            legendFormat='{{version}}',
                            refId='A')
                    ],
                    yAxes=[
                        G.YAxis(format=G.OPS_FORMAT),
                        G.YAxis(format=G.SHORT_FORMAT, show=False),
                    ],
                    nullPointMode=G.NULL_AS_ZERO,
                    stack=True,
                    lineWidth=0,
                    fill=10,
                    tooltip=G.Tooltip(valueType=G.INDIVIDUAL)),
                G.Graph(
                    title='Ballot latency',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='histogram_quantile(0.5, sum(irate(isaacranks_ballot_generation_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.5q',
                            refId='A'),
                        target(
                            expr='histogram_quantile(0.9, sum(irate(isaacranks_ballot_generation_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.9q',
                            refId='B'),
                        target(
                            expr='histogram_quantile(0.99, sum(irate(isaacranks_ballot_generation_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.99q',
                            refId='C'),
                    ],
                    yAxes=[G.YAxis(format=G.MILLISECONDS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)]),
            ]),
            G.Row(panels=[
                G.Graph(
                    title='Votes',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='sum(irate(isaacranks_vote_casting_seconds_count[5m])) by (version)',
                            legendFormat='{{version}}',
                            refId='A')
                    ],
                    yAxes=[G.YAxis(format=G.OPS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)],
                    nullPointMode=G.NULL_AS_ZERO,
                    stack=True,
                    lineWidth=0,
                    fill=10,
                    tooltip=G.Tooltip(valueType=G.INDIVIDUAL)),
                G.Graph(
                    title='Vote latency',
                    dataSource='prometheus',
                    targets=[
                        target(
                            expr='histogram_quantile(0.5, sum(irate(isaacranks_vote_casting_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.5q',
                            refId='A'),
                        target(
                            expr='histogram_quantile(0.9, sum(irate(isaacranks_vote_casting_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.9q',
                            refId='B'),
                        target(
                            expr='histogram_quantile(0.99, sum(irate(isaacranks_vote_casting_seconds_bucket{{service="{}-isaacranks"}}[5m])) by (le)) * 1000',
                            legendFormat='0.99q',
                            refId='C'),
                    ],
                    yAxes=[G.YAxis(format=G.MILLISECONDS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)]),
            ]),
            G.Row(panels=[
                G.Graph(
                    title='Time since last rebuild',
                    dataSource='prometheus',
                    targets=[target(
                        expr='time() - (isaacranks_last_rebuild_timestamp{{service="{}-rebuild"}} != 0)',
                        legendFormat='Age')],
                    legend=G.Legend(current=True),
                    yAxes=[G.YAxis(format=G.SECONDS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)]),
                G.Graph(
                    title='Rebuild duration',
                    dataSource='prometheus',
                    targets=[target(
                        expr='isaacranks_last_rebuild_duration_seconds{{service="{}-rebuild"}} != 0',
                        legendFormat='Duration')],
                    legend=G.Legend(current=True),
                    yAxes=[G.YAxis(format=G.SECONDS_FORMAT),
                           G.YAxis(format=G.SHORT_FORMAT, show=False)]),
            ])
        ]).auto_panel_ids()
