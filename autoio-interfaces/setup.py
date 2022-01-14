""" Install Interfaces to Programs:
        autorun, elstruct
        chemkin, intder, mess, nst, projrot,
        pac99, thermp, varecof
"""

from distutils.core import setup


setup(
    name="autoio-interfaces",
    version="0.10.0",
    packages=[
        'autorun',
        'elstruct',
        'elstruct.writer',
        'elstruct.reader',
        'elstruct.writer._cfour2',
        'elstruct.reader._cfour2',
        'elstruct.writer._gaussian09',
        'elstruct.reader._gaussian09',
        'elstruct.writer._molpro2015',
        'elstruct.reader._molpro2015',
        'elstruct.writer._mrcc2018',
        'elstruct.reader._mrcc2018',
        'elstruct.writer._nwchem6',
        'elstruct.reader._nwchem6',
        'elstruct.writer._orca4',
        'elstruct.reader._orca4',
        'elstruct.writer._psi4',
        'elstruct.reader._psi4',
        'elstruct.writer._qchem5',
        'elstruct.reader._qchem5',
        'chemkin_io',
        'chemkin_io.writer',
        'chemkin_io.parser',
        'intder_io',
        'mess_io',
        'mess_io.writer',
        'mess_io.reader',
        'nst_io',
        'onedmin_io',
        'pac99_io',
        'polyrate_io',
        'projrot_io',
        'thermp_io',
        'varecof_io',
        'varecof_io.writer',
        'varecof_io.reader'
    ],
    package_dir={
        'autorun': 'autorun',
        'elstruct': 'elstruct',
        'chemkin_io': 'chemkin_io',
        'intder_io': 'intder_io',
        'mess_io': 'mess_io',
        'nst_io': 'nst_io',
        'onedmin_io': 'onedmin_io',
        'pac99_io': 'pac99_io',
        'polyrate_io': 'polyrate_io',
        'projrot_io': 'projrot_io',
        'thermp_io': 'thermp_io',
        'varecof_io': 'varecof_io',
    },
    package_data={
        'autorun': ['aux/*',
                    'extern/*',
                    'tests/data/*'],
        'elstruct': ['writer/_cfour2/templates/*.mako',
                     'writer/_gaussian09/templates/*.mako',
                     'writer/_molpro2015/templates/*.mako',
                     'writer/_mrcc2018/templates/*.mako',
                     'writer/_nwchem6/templates/*.mako',
                     'writer/_orca4/templates/*.mako',
                     'writer/_psi4/templates/*.mako',
                     'writer/_qchem5/templates/*.mako'],
        'intder_io': ['templates/*.mako',
                      'tests/data/*'],
        'mess_io': ['writer/templates/sections/*.mako',
                    'writer/templates/sections/energy_transfer/*.mako',
                    'writer/templates/sections/monte_carlo/*.mako',
                    'writer/templates/sections/reaction_channel/*.mako',
                    'writer/templates/species/*.mako',
                    'writer/templates/species/info/*.mako',
                    'tests/data/inp/*',
                    'tests/data/out/*'],
        'nst_io': ['templates/*.mako',
                   'tests/data/*'],
        'onedmin_io': ['templates/*.mako',
                       'tests/data/*'],
        'pac99_io': ['tests/data/*'],
        'polyrate_io': ['templates/*.mako',
                        'tests/data/*'],
        'projrot_io': ['templates/*.mako',
                       'tests/data/*'],
        'thermp_io': ['templates/*.mako',
                      'tests/data/*'],
        'varecof_io': ['writer/templates/*.mako',
                       'tests/data/*']
    }
)
