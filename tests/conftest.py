# -*- coding: utf-8 -*-
# :Project:   python-rapidjson -- Tests configuration
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   MIT License
# :Copyright: © 2016, 2017 Lele Gaifax
#

import io
import rapidjson as rj


def pytest_generate_tests(metafunc):
    if 'dumps' in metafunc.fixturenames and 'loads' in metafunc.fixturenames:
        metafunc.parametrize('dumps,loads', (
            ((rj.dumps, rj.loads),
             (lambda o,**opts: rj.Encoder(**opts)(o),
              lambda j,**opts: rj.Decoder(**opts)(j)))
        ), ids=('func[string]',
                'class[string]'))
    elif 'dumps' in metafunc.fixturenames:
        metafunc.parametrize('dumps', (
            rj.dumps,
            lambda o,**opts: rj.Encoder(**opts)(o)
        ), ids=('func[string]',
                'class[string]'))
    elif 'loads' in metafunc.fixturenames:
        metafunc.parametrize('loads', (
            rj.loads,
            lambda j,**opts: rj.load(io.BytesIO(j.encode('utf-8')
                                           if isinstance(j, str) else j), **opts),
            lambda j,**opts: rj.Decoder(**opts)(j),
            lambda j,**opts: rj.Decoder(**opts)(io.BytesIO(j.encode('utf-8')
                                                      if isinstance(j, str) else j)),
        ), ids=('func[string]',
                'func[stream]',
                'class[string]',
                'class[stream]'))
