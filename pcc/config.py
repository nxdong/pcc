import os
import platform

PYTHON_EXT = ['.py']
PYTHON_NAME = 'python'
C_EXT = ['.c']
C_NAME = 'c'
SUPPORT_LANGUAGE = [
    (PYTHON_NAME, PYTHON_EXT),
    (C_NAME, C_EXT)
]


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


def detect_platform():
    return '{}-{}'.format(platform.system(), platform.machine())


def get_version():
    # TODO: uniform version
    return '0.0.2'


def get_lib_name():
    p = platform.system()
    if p == 'Linux':
        return 'libpcc_ts_all.so'
    elif p == 'Darwin':
        return 'libpcc_ts_all.dylib'
    elif p == 'Windows':
        return 'libpcc_ts_all.dll'
    elif p == 'Java':
        raise Exception("{} platform not support yet!", p)


PCC_DEFAULT_LIB_PATH = os.environ.get('PCC_DEFAULT_LIB_PATH', '.pcc/')
PCC_DEFAULT_LIB_NAME = os.environ.get('PCC_DEFAULT_LIB_NAME', get_lib_name())
PCC_DEFAULT_LIB_URL = os.environ.get(
    'PCC_DEFAULT_LIB_URL', 'https://nxdong.com/data/pcc/{}/{}/{}'.format(get_version(), detect_platform(), PCC_DEFAULT_LIB_NAME))

PCC_LIB_PATH = PCC_DEFAULT_LIB_PATH
PCC_LIB_NAME = PCC_DEFAULT_LIB_NAME

DEFAUTL_JOBS_COUNT = max(1, os.cpu_count()-2)
DEFAUTL_RESULT_COUNT = 10
