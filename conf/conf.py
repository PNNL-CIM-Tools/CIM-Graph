# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# General information about the project.
project = 'CIMantic Graphs'
copyright = '2025, Battelle Memorial Institute, All rights reserved.'
author = 'Alex Anderson & CIMantic Graphs Team'

# The full version, including alpha/beta/rc tags
release = '0.3.1a0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_parser']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Don't execute notebook contents when writing to html
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

# Use LuaLaTex
latex_engine = 'lualatex'

# Configure nbsphinx
nbsphinx_execute = 'auto'  # Set to 'auto', 'always', or 'never' as needed

# Add CSS to hide cells with hide_input tag
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

.. raw:: html

    <style>
        /* Hide input cells with hide_input tag */
        div.nbinput.container div.prompt.container.hide_input + div.input_area {
            display: none;
        }

        /* Alternative selector that should work with newer nbsphinx */
        .tag_hide_input .jp-CodeCell-inputWrapper {
            display: none !important;
        }

        /* For nbsphinx 0.8.0+ */
        .tag_hide_input .nbinput {
            display: none !important;
        }
    </style>
"""

# Configure tag-based cell filtering
nbsphinx_preprocessor_config = {
    'TagRemovePreprocessor': {
        'enabled': True,
        'remove_input_tags': {'hide_input'},
    }
}

# Additional options for fine-grained control
nbsphinx_execute_arguments = [
    '--TagRemovePreprocessor.enabled=True',
    "--TagRemovePreprocessor.remove_cell_tags={'hide_cell'}", # Hide the entire cell
    "--TagRemovePreprocessor.remove_input_tags={'hide_input'}", # Hide only the input
    "--TagRemovePreprocessor.remove_output_tags={'hide_output'}", # Hide only the output
]
