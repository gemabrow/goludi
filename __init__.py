__license__ = 'AGPL 3'
__copyright__ = '2018, gemabrow <gerald@geraldcodes.com>'

from calibre.customize import InterfaceActionBase

class GooglibrePluginMetadata(InterfaceActionBase):

    name                = 'Goog·li·bre'
    description         = 'Upload and download titles to/from Google Books'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'Gerald M. Brown' # The author of this plugin
    version             = (1, 0, 0)   # The version number of this plugin
    file_types          = set(['epub', 'pdf']) # The file types that this plugin will be applied to
    drm_free_only = True
    minimum_calibre_version = (0, 7, 53)

    # Plugin starts in 'main.py' - class GooglibrePlugin
    actual_plugin = 'calibre_plugins.googlibre.main:GooglibrePlugin'
