import json
from os import listdir
from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks
from twisted.python.procutils import which
from twisted.internet.utils import getProcessOutput
from txkube import network_kubernetes_from_context
from pyrsistent import pmap


def wrap_dashboard(out):
    dash = json.loads(out)
    return json.dumps({
        u'dashboard': dash,
        u'overwrite': True,
        }, indent=4).decode('utf-8')


@react
@inlineCallbacks
def main(reactor):
    dashboards = {}
    generate_dashboard = which(u'generate-dashboard')[0]
    for dash_file in listdir(u'.'):
        if not dash_file.endswith(u'.dashboard.py'):
            continue
        dash_name = dash_file[:-len(u'.dashboard.py')]
        out = yield getProcessOutput(
            generate_dashboard,
            [u'-o', u'/dev/stdout', dash_file],
            reactor=reactor)
        dashboards[dash_name + u'-dashboard.json'] = wrap_dashboard(out)
    dashboards[u'prometheus-datasource.json'] = json.dumps({
        'access': 'proxy',
        'basicAuth': False,
        'name': 'prometheus',
        'type': 'prometheus',
        'url': 'http://prometheus-global.default.svc:9090',
        }, indent=4).decode('utf-8')

    k8s = network_kubernetes_from_context(
        reactor,
        u'gke_decisive-cinema-167507_europe-west1-d_cluster-1')
    client = yield k8s.versioned_client()
    yield client.replace(client.model.v1.ConfigMap(
        metadata=pmap(
            {u'name': u'grafana-dashboards', u'namespace': u'default'}),
        data=pmap(dashboards)))


if __name__ == '__main__':
    main()
