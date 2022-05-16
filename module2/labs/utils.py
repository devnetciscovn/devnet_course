def build_config(customer):
    name = customer['name']
    rd = customer['rd']
    rt_import = customer['rt-import']
    rt_export = customer['rt-export']

    config = f"""vrf {name}
    rd {rd}
    address-family ipv4
    rt-import {rt_import}
    rt-export {rt_export}
    """
    return config

vietcombank = {
    'name': 'vietcombank',
    'rd': '65001:1',
    'rt-import': '65001:11',
    'rt-export': '65001:12',
    'interface': 'GE0/0/2',
    'ip': '192.168.1.1/24',
    'static_routes':
        {
            'next_hop': '192.168.3.200',
            'nets': ['10.0.0.0/16', '11.0.0.0/16', '14.3.0.0/16']
        }
}

vietinbank = {
    'name': 'vietinbank',
    'rd': '65001:2',
    'rt-import': '65001:21',
    'rt-export': '65001:22',
    'interface': 'GE0/0/2',
    'ip': '192.168.2.1/24',
    'static_routes':
        {
            'next_hop': '192.168.3.200',
            'nets': ['21.0.0.0/16', '22.0.0.0/16', '35.3.0.0/16']
        }
}

agribank = {
    'name': 'agribank',
    'rd': '65001:3',
    'rt-import': '65001:31',
    'rt-export': '65001:32',
    'interface': 'GE0/0/3',
    'ip': '192.168.3.1/24',
    'static_routes':
        {
            'next_hop': '192.168.3.200',
            'nets': ['20.0.0.0/16', '21.0.0.0/16', '34.3.0.0/16']
        }
}