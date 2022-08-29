# compile tree sitter dynamic library

## init submodule

```bash
# in repo root dir
git submodule init
```

## compile

```bash

```

## add new language support

found language in [tree-sitter group](https://github.com/tree-sitter) 
and add to submodule
```bash
git submodule add https://github.com/tree-sitter/tree-sitter-c languages/tree-sitter-c
```

## TODO

- add target platform detect
- add cross compile
- user needn't c/c++ compiler

