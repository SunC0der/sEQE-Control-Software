# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import pathlib
import sys
#sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, pathlib.Path(__file__))
sys.path.insert(0, pathlib.Path(__file__).parents[1].resolve().as_posix())
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AFMDs sEQE setup'
copyright = '2022, Anna Jungbluth'
author = 'Anna Jungbluth and Maximilian Hanauske'
release = 'October 2022'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   'sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary',
   'sphinx.ext.napoleon',
   'sphinx.ext.viewcode',
#   'sphinxcontrib.pdfembed',
   'sphinx.ext.autosectionlabel',
   'sphinx.ext.githubpages',

]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static','_assets']
html_logo = "AFMD_logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
