from setuptools import setup, find_packages
import os

version = '0.2dev'

setup(name='opkode.rateablediscussion',
      version=version,
      description="Allows plone.app.discussion comments to be rated.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='discussion comment rating',
      author='JC Brand',
      author_email='jc@opkode.com',
      url='http://opkode.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['opkode'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'simplejson',
          'plone.app.discussion',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
