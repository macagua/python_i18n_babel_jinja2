#!/usr/bin/env python
# -*- coding:utf-8 -*-

import i18n

if __name__ == '__main__':
    
    # Set locale to English
    i18n.setLocale("en")
    print(i18n.gettext("Home"))
    print(i18n.gettext("Canon"))
    print(i18n.gettext("About"))
    print(i18n.gettext("Setting"))
    print(i18n.gettext("Translation"))
    print("\n-----\n")
    
    # Set locale to Spanish
    i18n.setLocale("es")
    print(i18n.gettext("Home"))
    print(i18n.gettext("Canon"))
    print(i18n.gettext("About"))
    print(i18n.gettext("Setting"))
    print(i18n.gettext("Translation"))
    print("\n-----\n")

    # Set locale to Brazilian Portuguese
    i18n.setLocale("pt_BR")
    print(i18n.gettext("Home"))
    print(i18n.gettext("Canon"))
    print(i18n.gettext("About"))
    print(i18n.gettext("Setting"))
    print(i18n.gettext("Translation"))
