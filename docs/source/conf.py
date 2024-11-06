# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Photon Mapping'
copyright = '2024, Tuan-Minh NGUYEN, Aurélien BESNIER'
author = 'Tuan-Minh NGUYEN, Aurélien BESNIER'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'autoapi.extension', "sphinx_copybutton", "nbsphinx", "sphinx.ext.githubpages"]

templates_path = ['_templates']
exclude_patterns = []

autoapi_dirs = ['../../src/openalea']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
  "header_links_before_dropdown": 6,
  "sidebarwidth": 200,
  "collapse_navigation": "false",
  "icon_links": [
    {
        "name": "GitHub",
        "url": "https://github.com/openalea-incubator/photon_mapping",
        "icon": "fa-brands fa-github",
    },
    ],

    "show_version_warning_banner": True,
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
  }

# If false, no module index is generated.
html_domain_indices = True
# If false, no index is generated.
html_use_index = True
# If true, the index is split into individual pages for each letter.
html_split_index = False
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

html_static_path = ['_static']