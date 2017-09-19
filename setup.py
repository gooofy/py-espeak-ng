#!/usr/bin/env python

from setuptools import setup, find_packages

EXCLUDED = ['*.tests', '*.tests.*', 'tests.*', 'tests']

setup(name         ='espeakng',
      version      ='0.1.0',
      description  ='Python interface for eSpeak NG',
      classifiers  = [
                      'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                      'Topic :: Multimedia :: Sound/Audio :: Speech',
                      'Operating System :: POSIX :: Linux',
                      'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                     ],
      platforms    = 'Linux',
      license      = 'LGPLv3',
      package_dir  = {'espeakng': 'espeakng'},
      test_suite   = 'tests',
      packages     = find_packages('.', EXCLUDED),
      author       = "Guenter Bartsch",
      author_email = "guenter@zamia.org",
      )

