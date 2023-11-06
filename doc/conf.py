import sys, os
import sphinx_rtd_theme

sys.path.append(os.path.abspath('sphinxext'))

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


language = 'zh_CN'
author = 'DingJing'
project = 'Kernel Docs'
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
copyright = 'Copyright 2023 DingJing'


extensions = [
        'myst_parser',
]

exclude_patterns = []
templates_path = ['_templates']
html_static_path = ['_static']

html_theme_options = {

}


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
