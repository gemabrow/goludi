__license__ = 'GPL v3'
__copyright__ = '2018, gemabrow <gerald@geraldcodes.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

class InterfaceGooglibre(InterfaceActionBase):

    name = 'Goog·li·bre'
    version = (1, 0, 0)
    description = 'Upload and download titles to/from Google Books'
    author = 'Gerald M. Brown'
    minimum_calibre_version = (0, 7, 53)
    supported_platforms = ['windows', 'osx', 'linux']

    # Plugin starts in 'main.py' - class GooglibrePlugin
    actual_plugin = 'calibre_plugins.googlibre.main:GooglibrePlugin'

    def is_customizable(self):
        pass

    def config_widget(self):
        # from calibre_plugins.googlibre.config import ConfigWidget
        # return ConfigWidget()
        pass

    def save_settings(self, config_widget):
        # config_widget.save_settings()
        # ac = self.actual_plugin
        # if ac is not None:
        #     ac.apply_settings()
        pass
