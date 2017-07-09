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
    title='Isaac Ranks (test)',
    rows=[
        G.Row(panels=[
            G.SingleStat(
                title='Pods up (web)',
                dataSource='prometheus',
                valueName='current',
                sparkline=G.SparkLine(show=True),
                targets=[G.Target(expr='count by(service) (up{service="isaacranks-test-isaacranks"} == 1)')]),
            G.SingleStat(
                title='Pods up (rebuild)',
                dataSource='prometheus',
                valueName='current',
                sparkline=G.SparkLine(show=True),
                targets=[G.Target(expr='count by(service) (up{service="isaacranks-test-rebuild"} == 1)')]),
            ]),
        G.Row(panels=[
            G.Graph(
                title='HTTP RPS',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="isaacranks-test-isaacranks",status_code=~"1.."}[5m]))',
                        legendFormat='1xx',
                        refId='A'),
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="isaacranks-test-isaacranks",status_code=~"2.."}[5m]))',
                        legendFormat='2xx',
                        refId='B'),
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="isaacranks-test-isaacranks",status_code=~"3.."}[5m]))',
                        legendFormat='3xx',
                        refId='C'),
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="isaacranks-test-isaacranks",status_code=~"4.."}[5m]))',
                        legendFormat='4xx',
                        refId='D'),
                    G.Target(
                        expr='sum(irate(http_request_duration_seconds_count{service="isaacranks-test-isaacranks",status_code=~"5.."}[5m]))',
                        legendFormat='5xx',
                        refId='E'),
                    ],
                aliasColors=ALIAS_COLORS,
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
                title='HTTP latency',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='histogram_quantile(0.5, sum(irate(http_request_duration_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.5q',
                        refId='A'),
                    G.Target(
                        expr='histogram_quantile(0.9, sum(irate(http_request_duration_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.9q',
                        refId='B'),
                    G.Target(
                        expr='histogram_quantile(0.99, sum(irate(http_request_duration_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.99q',
                        refId='C'),
                    ],
                aliasColors=ALIAS_COLORS,
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                    ]),
            ]),
        G.Row(panels=[
            G.Graph(
                title='Ballots',
                dataSource='prometheus',
                targets=[
                    G.Target(
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
                    G.Target(
                        expr='histogram_quantile(0.5, sum(irate(isaacranks_ballot_generation_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.5q',
                        refId='A'),
                    G.Target(
                        expr='histogram_quantile(0.9, sum(irate(isaacranks_ballot_generation_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.9q',
                        refId='B'),
                    G.Target(
                        expr='histogram_quantile(0.99, sum(irate(isaacranks_ballot_generation_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.99q',
                        refId='C'),
                    ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                    ]),
            ]),
        G.Row(panels=[
            G.Graph(
                title='Votes',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='sum(irate(isaacranks_vote_casting_seconds_count[5m])) by (version)',
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
                title='Vote latency',
                dataSource='prometheus',
                targets=[
                    G.Target(
                        expr='histogram_quantile(0.5, sum(irate(isaacranks_vote_casting_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.5q',
                        refId='A'),
                    G.Target(
                        expr='histogram_quantile(0.9, sum(irate(isaacranks_vote_casting_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.9q',
                        refId='B'),
                    G.Target(
                        expr='histogram_quantile(0.99, sum(irate(isaacranks_vote_casting_seconds_bucket{service="isaacranks-test-isaacranks"}[5m])) by (le)) * 1000',
                        legendFormat='0.99q',
                        refId='C'),
                    ],
                yAxes=[
                    G.YAxis(format=G.MILLISECONDS_FORMAT),
                    G.YAxis(format=G.SHORT_FORMAT, show=False),
                    ]),
            ]),
        ]).auto_panel_ids()
