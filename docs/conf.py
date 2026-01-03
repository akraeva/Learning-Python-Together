# Configuration file for the Sphinx documentation builder.
# pylint: disable=invalid-name

# -- Project information -----------------------------------------------------
project = "Learning Python Together"
copyright = "2025, nia"
author = "Anna"
release = "1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "ru"

# Путь к исходникам - ДО автодока!
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Автодокументация
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "add_module_names": False,
}

napoleon_google_docstring = True  # NumPy/Google стиль
napoleon_numpy_docstring = True  # Для сложных docstring

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]
html_show_sourcelink = False
add_module_names = False

html_theme_options = {
    "show_powered_by": False,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "style_external_links": True,
}
