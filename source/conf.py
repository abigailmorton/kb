# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Abby Jane\'s Knowledge Base'
copyright = '2025, Abby Jane'
author = 'Abby Jane'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "myst_parser",
        "alabaster",
]

source_suffix = {
        ".rst": "restructuredtext",
        ".md": "markdown",
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ["style.css"]

html_theme_options = {
    "description": "Abby Jane’s homegrown knowledge base: infra, Ghost notes, certs, and what 3 AM Abby keeps forgetting.",
    "fixed_sidebar": True,
    "page_width": "960px",
    "sidebar_width": "240px",

    # If you want your name at the top instead of just the project title
    "logo_name": True,

    # Nice subtle header link colors
    "link": "#c2185b",
    "link_hover": "#7b1fa2",

    # Optional footer text
    "show_relbars": False,
    "logo_name": True,
}

html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "searchbox.html",
    ],
}

html_use_modindex = False

html_theme_options = {
    "description": "infra, Ghost notes, certs, and what 3 AM Abby Jane keeps forgetting.",
    "fixed_sidebar": True,
    "logo_name": True,
    "show_relbars": False,
}

html_last_updated_fmt = ""
html_show_sphinx = False