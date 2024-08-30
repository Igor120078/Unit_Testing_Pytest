### Install Pytest

```
    pip install pytest
```

### Run the tests

```
    pytest app/tests/test_movies.py
```

### Run the tests with details in report

```
    pytest -v app/tests/test_movies.py
```

### Some options

-s Show Output, do not caputure
-x Stop after first failure
-k "expression" Only run tests that match expession (and fixtures)
-rs Show extra summary info for SKIPPED
-r chars Show extra test summary info as specified by chars:
(f)ailed, (E)error, (s)skipped, (x)failed, (X)passed
(w)pytest-warnings (p)passed, (P)passed with output,
(a)all except pP.

-v Verbose
-q, --quiet Less verbose

### Install Pytest Coverage plugin

```
    pip install pytest-cov
```

-l, --showlocals Show local variables in tracebacks

### Run the tests with coverage

```
    pytest --cov
    or
    pytest -v --cov
```
