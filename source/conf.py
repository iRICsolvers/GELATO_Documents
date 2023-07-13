# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GELATO example manual'
copyright = '2023, yasuyuki shimizu and Jonathan Mark Nelson'
author = 'yasuyuki shimizu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # ... other extensions
    'sphinx_search.extension',
    ]

templates_path = ['_templates']
exclude_patterns = ['build']

numfig = True

numfig_format = {
    'figure': 'Figure %s',
    'table':  'Table %s',
    'code-block':  'List %s',
}

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ['css/custom.css']