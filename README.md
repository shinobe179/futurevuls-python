# futurevuls-python

FutureVuls API library in Python. 

FutureVuls : https://vuls.biz/

## Supported API

- health
- cve
- server
    - GET /v1/server/uuid/{serverUuid}
    - GET /v1/server/{serverID}
    - GET /v1/servers
    - POST /v1/server/paste
    - DELETE /v1/server/{serverID}

## How to use

### Install

```
$ git clone https://github.com/shinobe179/futurevuls-python.git
$ cd futurevuls-python
$ pip install .
```

### Example

```python
import os
import futurevuls

token = os.environ['FUTUREVULS_TOKEN']

fv = futurevuls.FutureVulsAPIClient(token)

if fv.check_health():
    fv.get_servers()
```

## How to test

### Prerequirements

- FutureVuls account
- API Token(R/W)
- Test server
  - Overwrite ttest/test_params.py by your test server's infos

### Example

```
$ cd /path/to/futurevuls-python/test
$ make
```