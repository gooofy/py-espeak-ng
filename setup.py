#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name             ='py-espeak-ng',
      version          ='0.1.8',
      description      ='Python interface for eSpeak NG',
      long_description = open('README.adoc', encoding='utf-8').read(),
      url              ='https://github.com/gooofy/py-espeak-ng',
      classifiers      = [
                          'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                          'Topic :: Multimedia :: Sound/Audio :: Speech',
                          'Operating System :: POSIX :: Linux',
                          'License :: OSI Approved :: Apache Software License',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.4',
                         ],
      keywords         = 'eSpeak NG TTS text to speech interface',
      platforms        = 'Linux',
      license          = 'Apache',
      package_dir      = {'espeakng': 'espeakng'},
      packages         = ['espeakng'],
      author           = "Guenter Bartsch",
      author_email     = "guenter@zamia.org",
      )
