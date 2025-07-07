
.PHONY: test clean format

install:
    pip install -e ".[dev]"

test:
    pytest

format:
    black . --line-length 100

clean:
    find . -type d -name "__pycache__" -exec rm -r {} + || true
    rm -rf *.egg-info
