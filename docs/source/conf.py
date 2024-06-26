# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CheckNode'
copyright = '2023, Chun-Yen Chen'
author = 'Chun-Yen Chen'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx_design",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist"
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
