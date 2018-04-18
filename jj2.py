#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import jinja2
import i18n

# Load jinja2.ext.i18n extension, more details at
# http://jinja.pocoo.org/docs/2.10/extensions/#i18n-extension
env = jinja2.Environment(
    # set the view folder that contains HTML files
    loader=jinja2.FileSystemLoader(
        [os.path.join(os.path.dirname(__file__), 'view')]
    ),
    extensions=['jinja2.ext.i18n'])

# Installs a translation globally for that environment.
env.install_gettext_translations(i18n)

if __name__ == '__main__':
    
    # Set HTML template
    template = env.get_template('index.html')

    # Set locale to English
    i18n.setLocale("en")
    # Print the HTML template with the previous language locale defined
    print(template.render())
    print("\n-----\n")

    # Set locale to Spanish
    i18n.setLocale("es")
    # Print the HTML template with the previous language locale defined
    print(template.render())
    print("\n-----\n")

    # Set locale to Brazilian Portuguese
    i18n.setLocale("pt_BR")
    # Print the HTML template with the previous language locale defined
    print(template.render())
