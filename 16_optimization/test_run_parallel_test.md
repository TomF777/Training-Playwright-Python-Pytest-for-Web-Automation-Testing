### Install pytest-xdist:
```
pip install pytest-xdist
```

### Run tests with specified number of workers:
```
pytest --numprocesses auto
```

### four workers in parallel
```
pytest --numprocesses 4
```
### auto assign number of workers:
```
pytest -n auto
```