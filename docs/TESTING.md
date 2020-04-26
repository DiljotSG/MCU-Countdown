# Testing

## Local Tests

Our local testing consists of unit tests, flake8 for linting and mypy
for type enforcement.

To automatically run all of these, install Tox using
```shell
pip3 install tox
```

and run the `tox` command in the main directory. 

To run a given kind of test individually, run:
```shell
tox -e [tests, flake8, mypy]
```

with your category of choice.
