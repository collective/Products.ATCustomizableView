# -*- coding: utf-8 -*-

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

originalCanSetLayout = BrowserDefaultMixin.canSetLayout

def cvCanSetLayout(self):
    if self.getProperty('fixed_layout', False):
        return False
    return originalCanSetLayout(self)