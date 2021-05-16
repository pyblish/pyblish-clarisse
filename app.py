#!/usr/bin/env python
# coding=utf-8
'''
Author: zuokangbo
Date: 2021-05-16 10:46:05
'''

# Standard library
import os

# Pyblish libraries
# import pyblish
import pyblish.api

# Import clarisse libraries
import ix

# Local libraries
from pyblish_clarisse import plugins
from PyQt5 import QtWidgets


def register_host():
    """Register supported hosts"""
    pyblish.api.register_host("clarisse")


def deregister_host():
    """Register supported hosts"""
    pyblish.api.deregister_host("clarisse")


def register_plugins():
    # Register accompanying plugins
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.register_plugin_path(plugin_path)
    print("pyblish: Registered %s" % plugin_path)


def deregister_plugins():
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.deregister_plugin_path(plugin_path)


def _discover_gui():
    """Return the most desirable of the currently registered GUIs"""

    # Prefer last registered
    guis = reversed(pyblish.api.registered_guis())

    for gui in guis:
        try:
            gui = __import__(gui)
        except (ImportError, AttributeError):
            continue
        else:
            return gui


def show(main_widget):
    """Try showing the most desirable GUI."""
    app = _discover_gui()
    app.settings.WindowTitle = "Pyblish (clarisse)"
    app.show(main_widget)


def setup():
    """Setup integration.

    Register plug-ins and integrate into the host

    """
    pyblish.api.register_gui('pyblish_lite')
    register_plugins()
    register_host()
    print("pyblish: Pyblish loaded successfully.")
    main_widget = get_main_widget()
    show(main_widget)


def get_main_widget():
    """Get qt instance."""
    return  QtWidgets.QApplication.instance()

