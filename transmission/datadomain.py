__version__ = "0.1"
# for this module's sphinx doc
release = __version__
version = release.rsplit('.', 1)[0]

from docutils import nodes
from sphinx import addnodes
from sphinx.util.docfields import Field
from sphinx.util import ws_re
from domaintools import custom_domain
import re

_data_node_re = re.compile(r'''(?x)
    \s*
    (?P<name>[^:]+)
    \s*
    :
    \s*
    (?P<type>[^=()]+)
    (?:
        \s*
        \(
        \s*
        (?P<type_comnt>[^=)]+)
        \s*
        \)
    )?
    \s*
    (?:
        \s*
        =
        \s*
        (?P<def>[^()]+)
        (?:
            \s*
            \(
            \s*
            (?P<def_comnt>[^)]+)
            \s*
            \)
        )?
        \s*
    )?
''')

def parse_data_node(env, sig, signode):
    m = _data_node_re.match(sig)
    if m is None:
        raise Exception('Invalid node sig')
    m = { k: v.strip() if v is not None else v for k, v in m.groupdict().items() }
    signode += addnodes.desc_name(m['name'], m['name'])
    if m['type'] is not None:
        signode += nodes.Text(' : ')
        signode += addnodes.desc_type(m['type'], m['type'])
        if m['type_comnt'] is not None:
            comnt = ' (' + m['type_comnt'] + ')'
            signode += nodes.emphasis(comnt, comnt)
    if m['def'] is not None:
        signode += nodes.Text(' = ')
        signode += nodes.Text(m['def'])
        if m['def_comnt'] is not None:
            comnt = ' (' + m['def_comnt'] + ')'
            signode += nodes.emphasis(comnt, comnt)
    return ws_re.sub('', m['name'])

def setup(app):
    app.add_domain(custom_domain('TransmissionJsonDomain',
        name  = 'trdata',
        label = "Structured Transmission data",

        elements = dict(
            settings_json = dict(
                objname = "settings.json",
                indextemplate = "settings.json; %s",
                parse = parse_data_node
            ),
            settings_plist = dict(
                objname = "org.m0k.transmission.plist",
                indextemplate = "org.m0k.transmission.plist; %s",
                parse = parse_data_node
            ),
        )))
