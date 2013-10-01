# -*- coding: utf-8 -*-

from Products.ATCustomizableView import logger

def uninstall(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.runAllImportStepsFromProfile('profile-Products.ATCustomizableView:uninstall')
    logger.info("Uninstall done")


