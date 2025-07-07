# tests/test_exporter.py

import os
import gzip
import json
import csv
from exporter import export_results

def test_export_json(tmp_path):
    data = ["línea 1", "línea 2"]
    export_results(data, format="json", compress=False, output_dir=tmp_path)
    files = list(tmp_path.glob("*.json"))
    assert len(files) == 1
    with open(files[0], encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == data

def test_export_csv(tmp_path):
    data = ["una línea", "otra línea"]
    export_results(data, format="csv", compress=False, output_dir=tmp_path)
    files = list(tmp_path.glob("*.csv"))
    assert len(files) == 1
    with open(files[0], encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows[0]["line"] == "una línea"

def test_compressed_export(tmp_path):
    data = ["algo comprimido"]
    export_results(data, format="json", compress=True, output_dir=tmp_path)
    files = list(tmp_path.glob("*.json.gz"))
    assert len(files) == 1
    with gzip.open(files[0], "rt", encoding="utf-8") as f:
        content = json.load(f)
    assert content == data
