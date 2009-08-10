# -*- coding: utf-8 -*-

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

originalCanSetDefaultPage = BrowserDefaultMixin.canSetDefaultPage

def cvCanSetDefaultPage(self):
    if self.getProperty('fixed_layout', False):
        return False
    return originalCanSetDefaultPage(self)

