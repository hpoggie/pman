import os

import pman


def test_get_conf(tmpdir):
    os.chdir(tmpdir.strpath)
    open('.pman', 'w').close()
    _ = pman.get_config()