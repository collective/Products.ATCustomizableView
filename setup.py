from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='Products.ATCustomizableView',
      version=version,
      description="A Plone monkey-patch for change the standard Plone behaviour with default view",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone atct default-view layout',
      author='Keul (Luca Fabbri)',
      author_email='luca.fabbri@redturtle.net',
      url='http://www.plone.it/scopri/documentazione/how-to/controllo-at-default-view-in-plone',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
