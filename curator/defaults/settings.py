import os
from voluptuous import *

# Elasticsearch versions supported
def version_max():
    return (5, 99, 99)
def version_min():
    return (5, 0, 0)

# Default Config file location
def config_file():
    return os.path.join(os.path.expanduser('~'), '.curator', 'curator.yml')

# Default filter patterns (regular expressions)
def regex_map():
    return {
        'timestring': r'^.*{0}.*$',
        'regex': r'{0}',
        'prefix': r'^{0}.*$',
        'suffix': r'^.*{0}$',
    }

def date_regex():
    return {
        'Y' : '4',
        'y' : '2',
        'm' : '2',
        'W' : '2',
        'U' : '2',
        'd' : '2',
        'H' : '2',
        'M' : '2',
        'S' : '2',
        'j' : '3',
    }

# Actions

def cluster_actions():
    return [ 'cluster_routing' ]

def index_actions():
    return [
        'alias',
        'allocation',
        'close',
        'create_index',
        'delete_indices',
        'forcemerge',
        'open',
        'reindex',
        'replicas',
        'rollover',
        'snapshot',
    ]

def snapshot_actions():
    return [ 'delete_snapshots', 'restore' ]

def all_actions():
    return sorted(cluster_actions() + index_actions() + snapshot_actions())

def index_filtertypes():
    return [
        'alias',
        'allocated',
        'age',
        'closed',
        'count',
        'forcemerged',
        'kibana',
        'none',
        'opened',
        'pattern',
        'space',
    ]

def snapshot_filtertypes():
    return ['age', 'count', 'none', 'pattern', 'state']

def all_filtertypes():
    return sorted(list(set(index_filtertypes() + snapshot_filtertypes())))

def default_options():
    return {
        'continue_if_exception': False,
        'disable_action': False,
        'ignore_empty_list': False,
        'timeout_override': None,
    }

def default_filters():
    return { 'filters' : [{ 'filtertype' : 'none' }] }

def structural_filter_elements():
    return {
        Optional('aliases'): Any(str, [str], unicode, [unicode]),
        Optional('allocation_type'): Any(str, unicode),
        Optional('count'): Coerce(int),
        Optional('direction'): Any(str, unicode),
        Optional('disk_space'): float,
        Optional('epoch'): Any(Coerce(int), None),
        Optional('exclude'): Any(int, str, unicode, bool, None),
        Optional('field'): Any(str, unicode, None),
        Optional('key'): Any(str, unicode),
        Optional('kind'): Any(str, unicode),
        Optional('max_num_segments'): Coerce(int),
        Optional('reverse'): Any(int, str, unicode, bool, None),
        Optional('source'): Any(str, unicode),
        Optional('state'): Any(str, unicode),
        Optional('stats_result'): Any(str, unicode, None),
        Optional('timestring'): Any(str, unicode, None),
        Optional('unit'): Any(str, unicode),
        Optional('unit_count'): Coerce(int),
        Optional('use_age'): Boolean(),
        Optional('value'): Any(int, float, str, unicode, bool),
    }