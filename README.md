# 🚀 log-optimizer-cli

> 🎛️ Herramienta de línea de comandos (CLI) para analizar, filtrar y exportar logs de servidor de forma estructurada y escalable.  
> 🎛️ Command-line tool (CLI) for analyzing, filtering, and exporting server logs in a structured and scalable way.

---

## 📚 Tabla de contenido / Table of Contents

- [📌 Características / Features](#-características--features)
- [🚀 Instalación / Installation](#-instalación--installation)
- [⚙️ Uso / Usage](#️-uso--usage)
- [📁 Estructura del Proyecto / Project Structure](#-estructura-del-proyecto--project-structure)
- [🧪 Tests](#-tests)
- [🪪 Licencia / License](#-licencia--license)

---

## 📌 Características / Features

- 🔍 Filtros configurables (fecha, nivel, patrones RegEx)  
  Configurable filters (date, level, RegEx patterns)
- 📤 Exportación a JSON o CSV  
  Export to JSON or CSV
- 🗜️ Compresión opcional con `.gz`  
  Optional `.gz` compression
- 🌐 Codificación personalizable (`utf-8`, `latin1`, etc.)  
  Customizable encoding
- 🐞 Logging interno para depuración  
  Internal logging for debug purposes
- 🧩 Arquitectura limpia y modular  
  Clean, modular architecture
- 📘 Documentación mínima y ejemplos de uso  
  Minimal documentation and usage examples
- 🧪 Tests unitarios básicos incluidos  
  Basic unit tests included

---

## 🚀 Instalación / Installation

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/log-optimizer-cli.git
cd log-optimizer-cli

# Crear entorno virtual
python3 -m venv .env
source .env/bin/activate  # En Windows: .env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

⚙️ Uso / Usage

# Filtrar por nivel de log y exportar a JSON
python main.py logs/input.log --level ERROR --export json

# Filtrar por fecha y comprimir salida
python main.py logs/*.log --from-date "2024-01-01" --to-date "2024-01-31" --compress

# Usar codificación personalizada y exportar a CSV
python main.py logs/ --encoding latin1 --export csv

📁 Estructura del Proyecto / Project Structure

log-optimizer-cli/
├── main.py             # CLI principal con Click
├── filters.py          # Lógica de filtrado
├── exporter.py         # Exportación y compresión
├── logger.py           # Configuración de logging interno
├── utils.py            # Utilidades varias
├── tests/              # Tests unitarios
├── README.md           # Este archivo
├── requirements.txt    # Dependencias mínimas
├── .gitignore
├── .gitattributes
└── LICENSE

🧪 Tests

# Ejecutar tests con pytest
pytest tests/

🪪 Licencia / License
Este proyecto está licenciado bajo los términos de la MIT License. This project is licensed under the terms of the MIT License.
