# Mysql-utils

Requirements :

- Python 3.X
- Mysql Server &&|| Client
- Balls

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

Simple queries:

```python
>>> from mysql_utils.queries import make_database, show_databases
>>> make_database('asample')
>>> print(show_databases())
<<< ['mysql', 'sys', 'asample'] # You might have other databases here
```

Advanced queries:

```python
>>> from mysql_utils.models import Database
>>> Database('mysql', 'asample')
<<< True, False
>>> Database('asample').create(force=False)
>>> Database('asample')
<<< True, True
```

Modeled queries:

```
```

## Documentation
