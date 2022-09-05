<div align="center">
    <h1><span style="color:#F42C04;">P</span>ython <span style="color:#F42C04;">C</span>yclomatic <span style="color:#F42C04;">C</span>omplexity <span style="color:#53687E;">Caculator</span></h1>
    <img src="https://img.shields.io/static/v1?label=version&message=0.0.1&color=green">
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
</div>

***


## Features

Cyclomatic complexity is a [code quality metric](https://en.wikipedia.org/wiki/Software_metric)

- multi charset support.(this may lead slow)
- pretty output


## Installation

```bash
pip install pcc-calc==0.0.1
```

you need download or build library first.




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
- depoly to pipy
- add c language
- add macos, windows support
- do more test
- comment support

## Reference

[Cookiecutter](https://github.com/audreyr/cookiecutter)
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
[cyclomatic complexities Wiki](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
[gocyclo](https://github.com/fzipp/gocyclo)
[tree-sitter](https://github.com/tree-sitter/tree-sitter)
[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
[mccabe](https://github.com/PyCQA/mccabe)
[cccalculator](https://github.com/xiaomizhou/cccalculator)

