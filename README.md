# mysql glob 0.3.7

Mysql Glob is a Python framework containing simple tools and models to administrate mysql server and manage their databases


Requirements :

- Python 3.*
- mysql-server or client


##### Status

(Currently tested under ubuntu and OSX systems)
python version: 3.6.1
mysql version: 5.7 (JSON support)

| Master | Dev | CodeCov |
| --- | --- | --- |
| [![CircleCI](https://circleci.com/gh/A-Hilaly/mysql-utils/tree/master.svg?style=svg&circle-token=7e0f4d185aee87f94eb656276862d74dfc0ce08f)](https://circleci.com/gh/A-Hilaly/mysql-utils/tree/master) | [![CircleCI](https://circleci.com/gh/A-Hilaly/mysql-utils/tree/dev.svg?style=svg&circle-token=7e0f4d185aee87f94eb656276862d74dfc0ce08f)](https://circleci.com/gh/A-Hilaly/mysql-utils/tree/dev) | [![codecov](https://codecov.io/gh/A-Hilaly/mysql-utils/branch/master/graph/badge.svg?token=a24hnSYvBi)](https://codecov.io/gh/A-Hilaly/mysql-utils) |

## Table of content

- [Status](#status)
- [Table of content](#table-of-content)
- [Installation](#build)
- [Configuration](#configuration)
- [Examples](#examples)
- [Documentation](#documentation)

## Installation


## configuration

## Examples

Simple functions

```python
>>> from mysql_glob.glob import make_database, show_databases
>>> make_database('db_1')
>>> show_database()
['mysql', 'sys', 'db_1'] # You might have other databases here

```

## Documentation
