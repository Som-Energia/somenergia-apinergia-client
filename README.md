# somenergia-apinergia-client

Package to read from SomEnergia Apinergia

# Usage

```python
from somenergia_apinergia.apinergia import Apinergia, Authentication

Authentication.set_url('https://apinergia.somenergia.coop')
username = 'MadamePoulain'
password = 'JeuxDenfants'

# check auth
token = Authentication().get_token(username, password)

api = Apinergia(base_url, username, password)

contractid = 12345678
cch_type = 'tg_cchval'
start_date = '2022-01-01'
end_date   = '2022-02-01'

result = api.get_cch_curves(contractid, cch_type, start_date, end_date)

print(result)
```

outputs:
```python
[
  {
    'contractId': '12345678', 'meteringPointId': '0ec1...a1',
    'measurements': {
      'season': 0, 'ai': 209, 'ao': 0, 'date': '2021-12-31 22:00:00+0000', 'dateDownload': '2022-01-04 02:43:43', 'dateUpdate': '2022-01-04 02:43:43'
      }
  },
  ...
  {
    'contractId': '12345678', 'meteringPointId': '0ec1...a1',
    'measurements': {
      'season': 0, 'ai': 115, 'ao': 0, 'date': '2022-01-31 22:00:00+0000', 'dateDownload': '2022-01-04 02:43:43', 'dateUpdate': '2022-01-04 02:43:43'
    }
  }
]
```

# Testing

requires pytest>=7 given that we use pythonpath option in pyproject.toml

```console
$ pytest
```

# Packaging

based on [PyPI doc](https://packaging.python.org/en/latest/tutorials/packaging-projects/) v:latest on Jun-2022

```console
$ pip install --upgrade build
$ python3 -m build
```

It might require

```console
$ sudo apt install python3.8-venv
```
## Distribute

```console
$ pip install --upgrade twine
```

### Distribute to TestPyPi

```console
$ twine upload --repository testpypi dist/*
```

### Distribute to PyPi

```console
$ twine upload dist/*
```
