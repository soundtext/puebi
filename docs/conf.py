# Configuration file for Sphinx documentation builder.
#
# Documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "EYD"
author = "EYD core team"
copyright = "2023–2026, EYD core team"
language = "id"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- EPUB options ------------------------------------------------------------

epub_show_urls = "footnote"

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "_static/.gitkeep",
    "_templates/.gitkeep",
]

# -- HTML output -------------------------------------------------------------

html_title = "Ejaan Bahasa Indonesia yang Disempurnakan (EYD) Edisi V"
html_short_title = "EYD V"

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
}

html_static_path = ["_static"]
