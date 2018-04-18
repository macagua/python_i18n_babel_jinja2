i18n Python Web Application by Babel and Jinja2
===============================================

Download
--------

.. code:: bash

    $ git clone https://github.com/macagua/python_i18n_babel_jinja2.git
    $ cd python_i18n_babel_jinja2

Installation
------------

.. code:: bash

    $ virtualenv .
    $ source ./bin/activate
    $ pip install -r requirements.txt --timeout 120

If the command has been correctly installed, a command should allow you to use the following command:

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

At the moment just compile message catalogs to MO files for finish the installation, 
executing the following command:

.. code:: bash

    $ pybabel compile -f -d ./locale
    compiling catalog ./locale/pt_BR/LC_MESSAGES/messages.po to ./locale/pt_BR/LC_MESSAGES/messages.mo
    compiling catalog ./locale/en/LC_MESSAGES/messages.po to ./locale/en/LC_MESSAGES/messages.mo
    compiling catalog ./locale/es/LC_MESSAGES/messages.po to ./locale/es/LC_MESSAGES/messages.mo

Running script
--------------

For running the Python script, execute the following command:

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


You can notice that the script prints by console each template in each supported translated language, 
in this case English, Spanish and Brazilian Portuguese.

Working with Babel
------------------

If you need extract new string to translate from the source code, execute the following command:

.. code:: bash

    $ pybabel extract -F ./locale/babel.cfg -o ./locale/messages.pot .

If you need initialize new language to translate from the POT file, execute the following command:

    $ pybabel init -l <LANG> -i ./locale/messages.pot -o ./locale/<LANG>/LC_MESSAGES/messages.po

If you update the new language or a language existing to translate from the POT file to PO file, execute the following command:

    $ pybabel update -l <LANG> -d ./locale -i ./locale/messages.pot

If you need compile compile message catalogs to binary MO files, execute the following command:

    $ pybabel compile -f -d ./locale

References
----------

- `i18n Python Web Application by gettext and Jinja2 <https://siongui.github.io/2016/01/17/i18n-python-web-application-by-gettext-jinja2/>`_.