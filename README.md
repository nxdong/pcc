<div align="center">
    <h1><span style="color:#F42C04;">P</span>ython <span style="color:#F42C04;">C</span>yclomatic <span style="color:#F42C04;">C</span>omplexity <span style="color:#53687E;">Caculator</span></h1>
    <h3>
        <a href="#Installation">Installation</a>
        <span> | </span>
        <a href="#Usage">Usage</a>
        <span> | </span>
        <a href="#Examples">Examples</a>
    </h3>
    <h5>
        <a href="./README.md">English</a>
        <span> | </span>
        <a href="./docs/README.zh-CN.md">简体中文</a>
    </h5>
    [![PyPI version](https://badge.fury.io/py/pcc-calc.svg)](https://badge.fury.io/py/pcc-calc)
</div>


***


## Features

Cyclomatic complexity is a [code quality metric](https://en.wikipedia.org/wiki/Software_metric)

- multi charset support.(this may lead slow)
- pretty output


## Installation

```bash
pip install pcc-calc==0.0.2
```

you need download or build library first.

```bash
pcc ./tests/data/python3 
Do you want to creat [/your/path/pcc/.pcc] ? [y/N]: y
Create Dir [/your/path/pcc/.pcc] success!
Do you want to dowload one from [/your/path/pcc/.pcc/libpcc_ts_all.so] ? [y/N]: y
Download [/your/path/pcc/.pcc] success!
                    Code Cyclomatic Complexity Caculator                                       
                                                                                                                 
| Complexity | Function          |                                                    File |
|------------|-------------------|---------------------------------------------------------|
|          6 | class             | /your/path/pcc/tests/data/python3/directory/class.py:15 |
|          6 | myfun             | /your/path/pcc/tests/data/python3/directory/class.py:32 |
|          6 | myfun2            | /your/path/pcc/tests/data/python3/directory/class.py:52 |
|          4 | function_in_file2 |  /your/path/pcc/tests/data/python3/directory/file2.py:1 |
|          2 | if_statment_0     |              /your/path/pcc/tests/data/python3/ifs.py:2 |
|          2 | if_statment_1     |              /your/path/pcc/tests/data/python3/ifs.py:8 |
|          2 | function_in_file1 |  /your/path/pcc/tests/data/python3/directory/file1.py:1 |
|          1 | get_url           |  /your/path/pcc/tests/data/python3/directory/class.py:7 |
|          1 | class             | /your/path/pcc/tests/data/python3/directory/class.py:12 |
                                                                                                                 
Procee [4] files use Time: 0.022909164428710938 s
```


## Usage

```bash
pcc --help
Usage: pcc [OPTIONS] CODE_PATH

  Cyclomatic Complexity Caculator

Options:
  -j, --jobs INTEGER            Parallel jobs count  [default: 10]
  -c, --count INTEGER           Output item count  [default: 10]
  -s, --sort BOOLEAN            sort by Complexity  [default: True]
  -e, --exclude_path DIRECTORY  exclude path
  --lib_path DIRECTORY          tree-sitter library path  [default: .pcc/]
  --version
  --help                        Show this message and exit.
```


## Examples

### caculate one file

```bash
pcc ./pcc/pcc.py
                               Code Cyclomatic Complexity Caculator

| Complexity | Function                       |                           File |
|------------|--------------------------------|--------------------------------|
|          2 | get_vistor                     |/your/project/pcc/pcc/pcc.py:19 |
|          2 | get_parser                     |/your/project/pcc/pcc/pcc.py:26 |
|          1 | detect_file_lanuage            |/your/project/pcc/pcc/pcc.py:14 |
|          1 | parse_code                     |/your/project/pcc/pcc/pcc.py:33 |
|          1 | calc_code_complexity           |/your/project/pcc/pcc/pcc.py:37 |
|          1 | calc_code_complexity_from_file |/your/project/pcc/pcc/pcc.py:49 |
```

### caculate directory

```bash
pcc . -j 8 -e ./venv -e ./docs -e ./languages
                                        Code Cyclomatic Complexity Caculator

| Complexity | Function              |                                                      File |
|------------|-----------------------|-----------------------------------------------------------|
|          7 | class                 |            /your/project/pcc/pcc/python/vistor_impl.py:94 |
|          7 | class                 |           /your/project/pcc/pcc/python/vistor_impl.py:117 |
|          7 | class                 |  /your/project/pcc/build/lib/pcc/python/vistor_impl.py:94 |
|          7 | class                 | /your/project/pcc/build/lib/pcc/python/vistor_impl.py:117 |
|          6 | travel_dir_and_filter |                         /your/project/pcc/pcc/utils.py:33 |
|          6 | check_or_download     |                           /your/project/pcc/pcc/cli.py:38 |
|          6 | class                 |/your/project/pcc/tests/data/python3/directory/class.py:15 |
|          6 | myfun                 |/your/project/pcc/tests/data/python3/directory/class.py:32 |
|          6 | myfun2                |/your/project/pcc/tests/data/python3/directory/class.py:52 |
|          6 | travel_dir_and_filter |               /your/project/pcc/build/lib/pcc/utils.py:33 |

Procee [37] files use Time: 0.04288077354431152 s
```

as u can see, `-e` can exclude directory you don't want, and can use multi times.

### multilang support

```bash
$ pcc ./tests/data/       
                  Code Cyclomatic Complexity Caculator                                       
                                                                                                                 
| Complexity | Function          |                                                                         File |
|------------|-------------------|------------------------------------------------------------------------------|
|          6 | class             | /home/sss/cyclomatic_complexity/pcc/tests/data/python3/directory/class.py:15 |
|          6 | myfun             | /home/sss/cyclomatic_complexity/pcc/tests/data/python3/directory/class.py:32 |
|          6 | myfun2            | /home/sss/cyclomatic_complexity/pcc/tests/data/python3/directory/class.py:52 |
|          4 | function_in_file2 |  /home/sss/cyclomatic_complexity/pcc/tests/data/python3/directory/file2.py:1 |
|          4 | ifs_c_func        |                     /home/sss/cyclomatic_complexity/pcc/tests/data/c/ifs.c:1 |
|          4 | if_c              |            /home/sss/cyclomatic_complexity/pcc/tests/data/c/directory/if.c:1 |
|          3 | for_c             |           /home/sss/cyclomatic_complexity/pcc/tests/data/c/directory/for.c:1 |
|          3 | if_while_c        |         /home/sss/cyclomatic_complexity/pcc/tests/data/c/directory/while.c:1 |
|          2 | if_statment_0     |              /home/sss/cyclomatic_complexity/pcc/tests/data/python3/ifs.py:2 |
|          2 | if_statment_1     |              /home/sss/cyclomatic_complexity/pcc/tests/data/python3/ifs.py:8 |
```

## Development

download repo and initialize environment

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements_dev.txt
# or use aliyun
pip3 install -r requirements_dev.txt -i https://mirrors.aliyun.com/pypi/simple/
git submodule update --init
```

compile dynamic library

```bash
make lib
```

run test

```bash
make test
```


## How to add new language support

1. add tree-sitter-parser project to languages dir
2. build new language so
3. add new dir in `pcc` dir like python.
4. implement node, parser, vistor for new language
5. add unit test

## TodoList

- add json output for future analyze
- add macos, windows support
- do more test
- comment support,for ignore function
- select language and sort group by language

## Reference

[Cookiecutter](https://github.com/audreyr/cookiecutter)  

[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)

[cyclomatic complexities Wiki](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

[gocyclo](https://github.com/fzipp/gocyclo)

[tree-sitter](https://github.com/tree-sitter/tree-sitter)

[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)

[mccabe](https://github.com/PyCQA/mccabe)

[cccalculator](https://github.com/xiaomizhou/cccalculator)



