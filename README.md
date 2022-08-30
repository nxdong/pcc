# pcc

![image](https://pypi.python.org/pypi/pcc)

![image](https://travis-ci.com/nxdong/pcc)

![Documentation Status](https://pcc.readthedocs.io/en/latest/?version=latest)

![Updates](https://pyup.io/repos/github/nxdong/pcc/)

Python Cyclomatic Complexity Caculator

## Features

Cyclomatic complexity is a [code quality metric](https://en.wikipedia.org/wiki/Software_metric)

​​圈复杂度(Cyclomatic Complexity)是一种代码复杂度的衡量标准。它可以用来衡量一个模块判定结构的复杂程度，数量上表现为独立线性路径条数，也可理解为覆盖所有的可能情况最少使用的测试用例数。圈复杂度大说明程序代码的判断逻辑复杂，可能质量低且难于测试和维护。

## Installation

## Usage

## Examples

## Development

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements_dev.txt
# or use aliyun
pip3 install -r requirements_dev.txt -i https://mirrors.aliyun.com/pypi/simple/
git submodule update --init
```

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

## Reference

[cyclomatic complexities Wiki](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
[gocyclo](https://github.com/fzipp/gocyclo)
[tree-sitter](https://github.com/tree-sitter/tree-sitter)
[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
[mccabe](https://github.com/PyCQA/mccabe)
