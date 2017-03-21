import os
import shutil

import click
import jinja2
import pdfkit
import yaml

__author__ = "Kevin Ciarniello"
__copyright__ = "Copyright 2017, Kevin Ciarniello"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kevin Ciarniello"
__email__ = "kciarnie@gmail.com"

# Template defaults
defaults = {
    'labels': None,
}


def get_theme_directory():
    """
    Gets the theme directory
    :return: a string of the themes directory
    """
    return os.path.abspath('theme')


def read_yaml(filename):
    """
    Reads the yaml file in and converts it to a yaml dict
    :param filename: the file to convert
    :return: a dictionary from the yaml
    """
    with open(filename, 'rt') as f:
        return yaml.load(f)


def render(filename, variables):
    """
    Grabs the jinja2 file and renders it
    :param filename: the jinja2 file to render
    :param variables:
    :return:
    """
    with open(filename, 'rt') as f:
        filename = jinja2.Template(f.read())

    return filename.render(**variables)


def jinja2_files(source, files):
    """
    Setup an ignore method for the copy, we want to ignore the .jinja2 files
    :param source: the source directory
    :param files: all the files from the source directory
    :return: a list of files that don't include .jinja2
    """
    return [filename for filename in files if filename.endswith('.jinja2')]


def build(data, config, output_dir):
    """
    Build the HTML or the PDF to the output_dir
    :param data:
    :param config:
    :param output_dir:
    :return:
    """
    variables = defaults.copy()
    variables.update(data)
    variables['config'] = config

    # Clean the output directory
    shutil.rmtree(output_dir, ignore_errors=True)

    # Copy
    shutil.copytree(get_theme_directory(), output_dir, ignore=jinja2_files)

    # Get all the .jinja2 files
    files = jinja2_files(None, os.listdir(get_theme_directory()))

    for filename in files:
        output_file = os.path.join(get_theme_directory(), filename)
        html = render(output_file, variables)

        # Create HTML type names
        rendered_file = filename.replace('.jinja2', '.html')

        # Remove any unusual characters
        output_html = html.encode('ascii', 'ignore').decode('ascii')

        # Write to the file
        with open(os.path.join(output_dir, rendered_file), 'w+') as f:
            f.write(output_html)


def generate_html(config, data):
    """
    Generate the HTML
    :param config:
    :param data:
    :return:
    """
    output_dir = config.get('output_dir', 'build')
    build(data, config, output_dir)


def generate_pdf(config, data):
    """
    Generate a PDF from the HTML file
    :param config:
    :param data:
    :return:
    """
    output_dir = config.get('output_dir', 'build')
    filename = config.get('name') + " " + str(config.get('year'))
    output_file = os.path.join(output_dir, filename.strip().replace(" ", "-") + '-resume.pdf')
    input_file = os.path.join(output_dir, 'index.html')

    if not os.path.exists(input_file):
        generate_html(config, data)

    print(input_file)

    if os.path.exists(input_file):
        convert_html_to_pdf(input_file, output_file)


def convert_html_to_pdf(source_html, output_filename):
    """
    Write the html to a PDF file
    :param source_html: the source HTML file
    :param output_filename: the output PDF file
    :return: the error status
    """
    # Generate PDF from a html file.
    pdfkit.from_file(source_html, output_filename)


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('resume_file', nargs=1, required=1, type=click.Path())
@click.option('--generate', '-g', default='html',
              help="Generate a type [default: html], html or pdf")
@click.option('--directory', '-d', default='build',
              help="Output directory for the build files. [default: build]")
def main(resume_file, generate, directory):
    """
    Entry function for the script to handle command arguments
    and run appropriate build like 'html' and 'pdf'.
    """

    # read resume data and config with some defaults
    resume_data = read_yaml(resume_file)
    config = resume_data.get('config', {})
    config.setdefault('output_dir', directory)

    # build based on the given format
    commands = {'html': generate_html, 'pdf': generate_pdf}

    return commands[generate](config, resume_data)


if __name__ == '__main__':
    main()
