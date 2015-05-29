from schemer import Schema
from schemer import Array


app_depends_schema = Schema({
    'services': {'type': Array(basestring)},
    'apps': {'type': Array(basestring)},
    'libs': {'type': Array(basestring)}
    })

host_forwarding_schema = Schema({
    'host_name': {'type': basestring},
    'host_port': {'type': int},
    'container_port': {'type': int}
    })

commands_schema = Schema({
    'always': {'type': basestring, 'required': True},
    'once': {'type': basestring}
    })

scripts_schema = Schema({

    })

app_schema = Schema({
    'repo': {'type': basestring, 'required': True},
    'depends': {'type': app_depends_schema},
    'host_forwarding': {'type': Array(host_forwarding_schema)},
    'image': {'type': basestring},
    'build': {'type': basestring},
    'mount': {'type': basestring},
    'commands': {'type': commands_schema},
    'scripts': {'type': scripts_schema},
    'compose': {'type': dict},
    })
