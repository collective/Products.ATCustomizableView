from Products.ATContentTypes.content.folder import ATFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

originalCanSetLayout = BrowserDefaultMixin.canSetLayout
originalCanSetDefaultPage = BrowserDefaultMixin.canSetDefaultPage

def cvCanSetLayout(self):
    if self.getProperty('fixed_layout', False):
        return False
    return originalCanSetLayout(self)

def cvCanSetDefaultPage(self):
    if self.getProperty('fixed_layout', False):
        return False
    return originalCanSetDefaultPage(self)

BrowserDefaultMixin.canSetLayout = cvCanSetLayout
BrowserDefaultMixin.canSetDefaultPage = cvCanSetDefaultPage

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
