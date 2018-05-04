#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2018, gemabrow <gerald@geraldcodes.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

class InterfaceGoludi(InterfaceActionBase):

    name                    = 'Go·lu·di'
    author                  = 'Gerald M. Brown'
    description             = 'Google Books for Calibre'
    supported_platforms     = ['windows', 'osx', 'linux']
    version                 = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)

    # Plugin starts in 'main.py' - class GooglibrePlugin
    actual_plugin = 'calibre_plugins.goludi.ui:GoludiPlugin'

    def is_customizable(self):
        '''
        This method must return True to enable customization via
        Preferences->Plugins
        '''
        return True

    def config_widget(self):
        '''
        Implement this method and :meth:`save_settings` in your plugin to
        use a custom configuration dialog.

        This method, if implemented, must return a QWidget. The widget can have
        an optional method validate() that takes no arguments and is called
        immediately after the user clicks OK. Changes are applied if and only
        if the method returns True.

        If for some reason you cannot perform the configuration at this time,
        return a tuple of two strings (message, details), these will be
        displayed as a warning dialog to the user and the process will be
        aborted.

        The base class implementation of this method raises NotImplementedError
        so by default no user configuration is possible.
        '''
        # It is important to put this import statement here rather than at the
        # top of the module as importing the config class will also cause the
        # GUI libraries to be loaded, which we do not want when using calibre
        # from the command line
        from calibre_plugins.goludi.config import ConfigWidget
        return ConfigWidget()

    def save_settings(self, config_widget):
        '''
        Save the settings specified by the user with config_widget.

        :param config_widget: The widget returned by :meth:`config_widget`.
        '''
        config_widget.save_settings()
        ac = self.actual_plugin
        if ac is not None:
            ac.apply_settings()
