i18n Python Web Application by Babel and Jinja2
===============================================

How to enable i18n support for Python Web Application using Babel and Jinja2.


Download
--------

For download the source code, please execute the follow command:

.. code:: bash

    $ git clone https://github.com/macagua/python_i18n_babel_jinja2.git
    $ cd python_i18n_babel_jinja2

Installation
------------

For install the source code, please execute the following commands:

.. code:: bash

    $ virtualenv .
    $ source ./bin/activate
    $ pip install -r requirements.txt --timeout 120

At the moment just compile message catalogs to MO files for finish the installation,
executing the following command:

Configuration
=============

For enable the *Internationalization and Localization* for this Sphinx Theme, you will need checkout 
the following configurations:

Translations files
------------------

The translations files are based on ``gettext`` format and they are placed at the 
``python_i18n_babel_jinja2/locale/`` directory, like it showing the following structure:

.. code:: bash

    python_i18n_babel_jinja2/locale/
    ├── en
    │   └── LC_MESSAGES
    │       ├── messages.mo
    │       └── messages.po
    ├── es
    │   └── LC_MESSAGES
    │       ├── messages.mo
    │       └── messages.po
    ├── pt_BR
    │   └── LC_MESSAGES
    │       ├── messages.mo
    │       └── messages.po
    ├── babel.cfg
    └── messages.pot

``python_i18n_babel_jinja2/locale/<LANG>/LC_MESSAGES/``
    This folder contains a specific language is the **Gettext format**.

``babel.cfg``
    This file is the **babel** configurations.

``messages.pot``
    This file is the **Portable Object Template** Gettext format.

``messages.po``
    This file is the **Portable Object** Gettext format to translate.

``messages.mo``
    This file is the **Machine Object** Gettext format generated later of translate 
    your ``messages.po`` file via the catalog compilation.

Babel extraction configurations
-------------------------------

First of all you have to get into the folder where you have your project and create a mapping file 
called ``babel.cfg`` into ``python_i18n_babel_jinja2/locale/`` directory that contains the 
**extraction from Jinja2 HTML templates** configurations. For typical Sphinx extensions, this is what 
you want in there:

.. code:: cfg

    # Extraction from Jinja2 HTML templates
    [jinja2: **/**.html]
    encoding = utf-8
    ignore_tags = script,style
    include_attrs = alt title summary placeholder


.. seealso::

    More details check out the following links:

    - `How setup this file <http://babel.pocoo.org/en/latest/setup.html>`_
    - `A previous file example description <http://babel.pocoo.org/en/latest/messages.html#extraction-method-mapping-and-configuration>`_


.. code:: bash

    $ pybabel compile -f -d ./locale
    compiling catalog ./locale/pt_BR/LC_MESSAGES/messages.po to ./locale/pt_BR/LC_MESSAGES/messages.mo
    compiling catalog ./locale/en/LC_MESSAGES/messages.po to ./locale/en/LC_MESSAGES/messages.mo
    compiling catalog ./locale/es/LC_MESSAGES/messages.po to ./locale/es/LC_MESSAGES/messages.mo

Web Application
===============

The struture directory for the Web Application is like the following:

``view/index.html``
    This is a HTML template based jinja2 engine.

``demo.py``
    This Python module is a Gettext demostration application.

``i18n.py``
    This Python module is an app for find out and print all supported languages available 
    in ``locale`` directory.

``jj2.py``
    This Python module is the main application.

Locales Python script
---------------------

For running the a Python script called ``i18n.py``, for show the languages available 
executing the following command:

.. code:: bash

    $ python ./i18n.py
    pt_BR
    en
    es

Running Python script
---------------------

For running the Python script called ``demo.py``, execute the following command:

.. code:: bash

    $ python ./demo.py 
    Home
    Canon
    About
    Setting
    Translation

    -----

    Inicio
    Canon
    Acerca de
    Configuración
    Traducción

    -----

    Home
    Canon
    Sobre
    Configuração
    Tradução

.. note::

    You can notice that the script prints by console each messages in each supported
    translated language, in this case *English*, *Spanish* and *Brazilian Portuguese*.

Running Web Application script
------------------------------

For running the Python Web Application script called ``jj2.py``, execute the following command:

.. code:: bash

    $ python ./jj2.py
    <!doctype html>
    <html>
        <head>
            <title>i18n Python Web Application by Babel and Jinja2</title>
        </head>
        <body>
            <div>Home</div>
            <div>News</div>
            <div>About</div>
            <div>Setting</div>
            <div>Translation</div>
        </body>
    </html>

    -----

    <!doctype html>
    <html>
        <head>
            <title>Internacionalización y localización de Aplicación Web Python con Babel y Jinja2</title>
        </head>
        <body>
            <div>Inicio</div>
            <div>Noticias</div>
            <div>Acerca de</div>
            <div>Configuración</div>
            <div>Traducción</div>
        </body>
    </html>

    -----

    <!doctype html>
    <html>
        <head>
            <title>Internacionalização e Localização do aplicativo da Web em Python por Babel e Jinja2</title>
        </head>
        <body>
            <div>Home</div>
            <div>Notícia</div>
            <div>Sobre</div>
            <div>Configuração</div>
            <div>Tradução</div>
        </body>
    </html>


.. note::

    You can notice that the script prints by console each HTML templates in each
    supported translated language, in this case *English*, *Spanish* and *Brazilian Portuguese*.

Working with Babel
------------------

If the command has been correctly installed ``babel`` package, a command should allow you to use 
the following command:

.. code:: bash

    $ pybabel subcommand options

Execute the follow command for more options and follow these instructions to get details:

.. code:: bash

    $  pybabel --help
    Usage: pybabel command [options] [args]

    Options:
      --version       show program's version number and exit
      -h, --help      show this help message and exit
      --list-locales  print all known locales and exit
      -v, --verbose   print as much as possible
      -q, --quiet     print as little as possible

    commands:
      compile  compile message catalogs to MO files
      extract  extract messages from source files and generate a POT file
      init     create new message catalogs from a POT file
      update   update existing message catalogs from a POT file

If you need extract new string to translate from the source code, execute the following command:

.. code:: bash

    $ pybabel extract -F ./locale/babel.cfg -o ./locale/messages.pot .

If you need initialize new language to translate from the POT file, execute the following command:

.. code:: bash

    $ pybabel init -l <LANG> -i ./locale/messages.pot -o ./locale/<LANG>/LC_MESSAGES/messages.po

If you update the new language or a language existing to translate from the POT file to PO file, execute the following command:

.. code:: bash

    $ pybabel update -l <LANG> -d ./locale -i ./locale/messages.pot

If you need compile compile message catalogs to binary MO files, execute the following command:

.. code:: bash

    $ pybabel compile -f -d ./locale

References
----------

- `i18n Python Web Application by gettext and Jinja2 <https://siongui.github.io/2016/01/17/i18n-python-web-application-by-gettext-jinja2/>`_.
