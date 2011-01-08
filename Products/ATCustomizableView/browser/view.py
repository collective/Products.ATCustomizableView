# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.ATCustomizableView import custommenuMessageFactory as _
from Products.CMFCore.utils import getToolByName

class CustomizeViewMenuView(BrowserView):
    """The view with form for customizing View menu"""

    template = ViewPageTemplateFile("customize-viewmenu.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.request.set('disable_border', True)

    def __call__(self, *args, **kw):
        return self.template()