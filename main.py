# main.py

import click
from filters import apply_filters
from exporter import export_results
from logger import setup_logger

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.option('--level', help="Nivel de log a filtrar (ej: INFO, WARNING, ERROR)")
@click.option('--from-date', help="Fecha desde (YYYY-MM-DD)")
@click.option('--to-date', help="Fecha hasta (YYYY-MM-DD)")
@click.option('--pattern', help="Patrón RegEx para buscar en los mensajes de log")
@click.option('--export', type=click.Choice(['json', 'csv']), default='json', help="Formato de exportación")
@click.option('--compress', is_flag=True, help="Comprimir salida con .gz")
@click.option('--encoding', default='utf-8', help="Codificación del archivo de salida")
@click.option('--log-file', type=click.Path(), help="Ruta del archivo de depuración interno")
def cli(input_path, level, from_date, to_date, pattern, export, compress, encoding, log_file):
    """CLI para analizar y exportar logs de servidor de forma estructurada"""
    logger = setup_logger(log_file)
    logger.info("Inicio de la ejecución")

    try:
        filtered_lines = apply_filters(
            input_path=input_path,
            level=level,
            from_date=from_date,
            to_date=to_date,
            pattern=pattern
        )

        export_results(
            data=filtered_lines,
            format=export,
            compress=compress,
            encoding=encoding
        )

        logger.info("Proceso finalizado con éxito")

    except Exception as e:
        logger.exception(f"Error durante la ejecución: {e}")
        click.echo(f"❌ Error: {e}")

if __name__ == '__main__':
    cli()
