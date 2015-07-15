# -*- coding: utf-8 -*-
#
# redaction-technique.org documentation build configuration file, created by
# sphinx-quickstart on Tue Oct 21 18:03:37 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'redaction-technique.org'
copyright = u'2015, Olivier Carrère'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '1'
# The full version, including alpha/beta/rc tags.
release = '1.5'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'fr'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_epilog = u"""

.. substitutions

.. |cms| replace:: :abbr:`CMS (Content Management System)`
.. |dita-ot| replace:: :abbr:`DITA-OT (DITA Open Toolkit)`
.. |ide| replace:: :abbr:`IDE (Integrated Development Environment)`

.. links

.. _Alfresco: http://www.alfresco.com/fr
.. _CSS: https://github.com/olivier-carrere/redaction-technique.org/tree/master/_static
.. _Componize: http://www.componize.com
.. _DITA Open Toolkit 1.5.4: http://sourceforge.net/projects/dita-ot/files/DITA-OT Stable Release/DITA Open Toolkit 1.5.4/DITA-OT1.5.4_full_easy_install_bin.zip/download
.. _DITA XML: https://github.com/olivier-carrere/redaction-technique.org/tree/DITA_XML
.. _DITA integration for Drupal: http://drupal.org/project/dita
.. _DocBook: https://github.com/olivier-carrere/redaction-technique.org/tree/DocBook
.. _DocZone: http://www.doczone.com
.. _FrameMaker: http://en.wikipedia.org/wiki/Adobe_FrameMaker
.. _Git: http://www.git-scm.com
.. _JPEG: http://fr.wikipedia.org/wiki/Jpeg
.. _LinkedIn: http://fr.linkedin.com/in/carrereolivier
.. _Java: http://java.com/fr/download/manual.jsp?locale=fr
.. _Makefile: https://github.com/olivier-carrere/redaction-technique.org/commits/master/Makefile
.. _NuFirewall: http://linuxfr.org/news/nufirewall-le-pare-feu-libre-sans-prise-de-t%C3%AAte
.. _OpenDocument: http://fr.wikipedia.org/wiki/OpenDocument
.. _Predictive: http://www.dr-qubit.org/emacs.php#predictive-download
.. _RAW: http://fr.wikipedia.org/wiki/RAW_(format_d%27image)
.. _Read the Docs: https://readthedocs.org/projects/redaction-techniqueorg
.. _SyncToy: http://www.microsoft.com/en-us/download/details.aspx?id=15155
.. _TIFF: http://fr.wikipedia.org/wiki/Tagged_Image_File_Format
.. _Trac: http://trac.edgewall.org
.. _Unison: http://www.cis.upenn.edu/~bcpierce/unison
.. _Viadeo: http://fr.viadeo.com/fr/profile/olivier.carrere
.. _XML::Twig: http://www.xmltwig.org/xmltwig/
.. _XPATH: http://fr.wikipedia.org/wiki/XPath
.. _XSD: http://fr.wikipedia.org/wiki/XML_Schema
.. _XSL-FO: http://fr.wikipedia.org/wiki/XSL-FO
.. _conref: http://docs.oasis-open.org/dita/v1.1/OS/archspec/conref.html
.. _ditaval: http://docs.oasis-open.org/dita/v1.2/os/spec/common/about-ditaval.html
.. _expressions rationnelles: http://fr.wikipedia.org/wiki/Expression_rationnelle
.. _l'archive des fichiers schemas.xml: http://www.redaction-technique.org/media/schemas.redaction-technique.org.tar.gz
.. _l'archive des schémas RelaxNG pour DITA XML: http://www.redaction-technique.org/media/rnc.tar.gz
.. _reStructuredText: https://github.com/olivier-carrere/redaction-technique.org/tree/master
.. _reltable: http://docs.oasis-open.org/dita/v1.0/langspec/reltable.html
.. _rsync: http://rsync.samba.org
.. _script de génération multilingue DITA XML: http://www.redaction-technique.org/media/dita2target.sh
.. _scripts Bash: https://github.com/olivier-carrere/redaction-technique.org/tree/master/scripts
.. _spécialisation: http://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture#Specialization
.. _topics: http://docs.oasis-open.org/dita/v1.0/archspec/topicover.html
.. _un point fort du produit: http://www.linformaticien.com/tests/id/20068/categoryid/48/edenwall-nufirewall-le-pare-feu-nouvelle-generation.aspx
.. _xinclude: http://en.wikipedia.org/wiki/XInclude
.. _xml_split: http://search.cpan.org/dist/XML-Twig/tools/xml_split/xml_split
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'agogo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "headerbg" : "grey"
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = u'Processus de rédaction technique - une approche pragmatique basée sur des solutions open-source'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "graphics/redaction-technique.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "graphics/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'redaction-techniqueorgdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

    'babel': '\\usepackage[francais]{babel}',
    'preamble': '\\usepackage{redaction-technique}',
    'classoptions': ',openany',
}

latex_additional_files = [
    '_themes/redaction-technique.sty',
    '_themes/wallpaper.sty',
 ]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'redaction-techniqueorg.tex', u'Processus de rédaction technique',
   u'Olivier Carrère', 'manual', 'toctree_only'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "graphics/redaction-technique.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'redaction-techniqueorg', u'redaction-technique.org Documentation',
     [u'Olivier Carrère'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'redaction-technique.org'
epub_author = u'Olivier Carrère'
epub_publisher = u'Olivier Carrère'
epub_copyright = u'2015, Olivier Carrère'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
