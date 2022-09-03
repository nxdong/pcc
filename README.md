# pcc

Python Cyclomatic Complexity Caculator

## Features

Cyclomatic complexity is a [code quality metric](https://en.wikipedia.org/wiki/Software_metric)

​​圈复杂度(Cyclomatic Complexity)是一种代码复杂度的衡量标准。它可以用来衡量一个模块判定结构的复杂程度，数量上表现为独立线性路径条数，也可理解为覆盖所有的可能情况最少使用的测试用例数。圈复杂度大说明程序代码的判断逻辑复杂，可能质量低且难于测试和维护。

- multi charset support.
- pretty output


## Installation

```bash

```

## Usage

```bash
pcc ./pcc/pcc.py
                               Code Cyclomatic Complexity Caculator                                
                                                                                                   
| Complexity | Function                       |                                              File |
|------------|--------------------------------|---------------------------------------------------|
|          2 | get_vistor                     | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:19 |
|          2 | get_parser                     | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:26 |
|          1 | detect_file_lanuage            | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:14 |
|          1 | parse_code                     | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:33 |
|          1 | calc_code_complexity           | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:37 |
|          1 | calc_code_complexity_from_file | /home/sss/cyclomatic_complexity/pcc/pcc/pcc.py:49 |
```

## Examples

## Development

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements_dev.txt
# or use aliyun
pip3 install -r requirements_dev.txt -i https://mirrors.aliyun.com/pypi/simple/
git submodule update --init

python3 ./languages/build_dynamic.py
```

test:

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

- add cli support
- add file/dir support
- more output theme
- multi thread support
- depoly to pipy
- add c language
- add macos, windows support
- add cross platform support
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

