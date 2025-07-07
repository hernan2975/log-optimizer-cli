# exporter.py

import json
import csv
import gzip
from datetime import datetime
from pathlib import Path

def export_results(data, format='json', compress=False, encoding='utf-8', output_dir='outputs'):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    extension = f".{format}"
    filename = f"logs_export_{timestamp}{extension}"
    output_path = Path(output_dir) / filename

    if compress:
        output_path = output_path.with_suffix(output_path.suffix + '.gz')

    if format == 'json':
        write_json(data, output_path, compress, encoding)
    elif format == 'csv':
        write_csv(data, output_path, compress, encoding)

    print(f"✅ Exportación finalizada: {output_path.resolve()}")

def write_json(data, path, compress, encoding):
    content = json.dumps(data, ensure_ascii=False, indent=2)
    _write_to_file(path, content, compress, encoding)

def write_csv(data, path, compress, encoding):
    csv_lines = ["line"]
    content = "\n".join([f'"{line.replace(chr(34), chr(34) * 2)}"' for line in data])
    content = f"{csv_lines[0]}\n{content}"
    _write_to_file(path, content, compress, encoding)

def _write_to_file(path, content, compress, encoding):
    mode = 'wt'
    open_func = gzip.open if compress else open
    with open_func(path, mode, encoding=encoding) as f:
        f.write(content)
