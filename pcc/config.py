import os

PYTHON_EXT = ['.py']
PYTHON_NAME = 'python'
SUPPORT_LANGUAGE = [(PYTHON_NAME, PYTHON_EXT)]


def _gen_ext_map():
    m = {}
    for lan_name, ext_list in SUPPORT_LANGUAGE:
        for ext in ext_list:
            if ext in m:
                raise Exception(
                    "Conflict ext name: {}, {} has already bind to {}.".format(m[ext], ext, lan_name))
            m[ext] = lan_name
    return m


FILE_EXT_MAP = _gen_ext_map()


PCC_DEFAULT_LIB_PATH = os.environ.get('PCC_DEFAULT_LIB_PATH', '.pcc/')
PCC_DEFAULT_LIB_NAME = os.environ.get('PCC_DEFAULT_LIB_NAME', 'pcc_ts_all.so')
PCC_DEFAULT_LIB_URL = os.environ.get(
    'PCC_DEFAULT_LIB_URL', 'https://nxdong.com/data/pcc/0.0.1/Linux-x86_64/libpcc_ts_all.so')

PCC_LIB_PATH = PCC_DEFAULT_LIB_PATH
PCC_LIB_NAME = PCC_DEFAULT_LIB_NAME
