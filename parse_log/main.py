import click
import os
from .utils.ParseLog import LogParser

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('filename')
@click.option('-t', '--type', 'file_type', help="output file's type")
@click.option('-o', '--output', 'path', help="output's path")
def cli(filename, file_type=None, path=None):
    """
    mytools is a cli tool to convert nginx's error log to JSON and TXT file.

    Basic Usage : 
\n
        $ mytools /var/log/nginx/error.log -t json
\n
        or
\n
        $ mytools /var/log/nginx/error.log -t text
\n
        or
\n
        $ mytools /var/log/nginx/error.log -t json -o /var/log/nginx/error.json
\n
        This command will generate text file as a default if -t or --type is not provided.
    """
    if path is None:
        path = ''
    Parser = LogParser(filename)
    Parser.save(file_type=file_type, output_path=path)
