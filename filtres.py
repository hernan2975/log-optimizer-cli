 # filters.py

import re
from datetime import datetime
from pathlib import Path

DATE_FORMAT = "%Y-%m-%d"

def parse_date(date_str):
    if date_str:
        return datetime.strptime(date_str, DATE_FORMAT)
    return None

def line_matches(line, level=None, from_date=None, to_date=None, pattern=None):
    if level and level not in line:
        return False

    if from_date or to_date:
        date_match = re.search(r"\d{4}-\d{2}-\d{2}", line)
        if not date_match:
            return False

        log_date = datetime.strptime(date_match.group(), DATE_FORMAT)

        if from_date and log_date < from_date:
            return False
        if to_date and log_date > to_date:
            return False

    if pattern and not re.search(pattern, line):
        return False

    return True

def apply_filters(input_path, level=None, from_date=None, to_date=None, pattern=None):
    input_path = Path(input_path)
    from_date = parse_date(from_date)
    to_date = parse_date(to_date)

    matched_lines = []

    files = [input_path] if input_path.is_file() else input_path.glob("*.log")

    for file in files:
        with file.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line_matches(line, level, from_date, to_date, pattern):
                    matched_lines.append(line.strip())

    return matched_lines
