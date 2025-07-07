# utils.py

def safe_strip(line):
    """Retorna la línea sin espacios y sin romper si es None"""
    return line.strip() if isinstance(line, str) else ''
