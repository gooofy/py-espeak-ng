#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import unittest
import logging
from io import StringIO, BytesIO
import wave

from espeakng import ESpeakNG

G2P_TESTS = [
             (u"GELBSEIDENEN",     u"dZ'ElbseId,En@n",     u"d͡ʒˈɛlbse͡ɪdˌɛnən"),
             (u"UNMUTE",           u"Vnmj'u:t",            u"ʌnmjˈuːt"),
             (u"GESCHIRRSCHEUERN", u"dZ'Esk3r-@Sj,u:3n",   u"d͡ʒˈɛskɚɹəʃjˌuːɚn"),
             (u"DÜSTRE",           u"d'u:st3",             u"dˈuːstɚ"),
             (u"EINGANGE",         u"'aINgandZ",           u"ˈa͡ɪŋɡænd͡ʒ"),
             (u"AUSSCHLÄGEN",      u"'O:SlEdZ@n",          u"ˈɔːʃlɛd͡ʒən"),
             (u"NACHHÄNGEND",      u"n'atSh@ndZ,End",      u"nˈæt͡ʃhənd͡ʒˌɛnd"),
             (u"HAUPTSTRAßEN",     u"h'O:ptst3r- 'as 'En", u"hˈɔːptstɚɹ ˈæs ˈɛn"),
             (u"HOCHWEISEN",       u"h'0tSwaIz@n",         u"hˈɑːt͡ʃwa͡ɪzən"),
             (u"DICKER",           u"d'Ik3",               u"dˈɪkɚ"),
            ]

class TestESpeakNG (unittest.TestCase):

    def test_say_en(self):

        esng = ESpeakNG(voice='english-us')
        esng.pitch = 32
        esng.speed = 150
        esng.say('Hello World!', sync=True)

    def test_say_de(self):

        esng = ESpeakNG(voice='german')
        esng.pitch = 32
        esng.speed = 150
        esng.say('Wie geht es Dir?', sync=True)

    def test_voices(self):
        esng = ESpeakNG()

        voices = esng.voices
        self.assertGreater (len(voices), 10)

    def test_synth_wav(self):

        esng = ESpeakNG(voice='english-us')
        esng.pitch = 32
        esng.speed = 150
        wavs = esng.synth_wav('Hello World!')
        wav = wave.open(BytesIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 22050)
        self.assertGreater (wav.getnframes(),   24000)

    def test_synth_wav_xsampa(self):

        esng = ESpeakNG(voice='english-us')
        esng.pitch = 32
        esng.speed = 150
        wavs = esng.synth_wav("h@l'oU", fmt='xs')
        wav = wave.open(BytesIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 22050)
        self.assertGreater (wav.getnframes(),   20000)

    def test_g2p(self):
        esng = ESpeakNG(voice='english-us')

        for g, xs_t, ipa_t in G2P_TESTS:

            xs  = esng.g2p (g)
            self.assertEqual(xs, xs_t)

            ipa = esng.g2p (g, ipa=2)
            self.assertEqual(ipa, ipa_t)

if __name__ == "__main__":

    logging.basicConfig(level=logging.ERROR)
    # logging.basicConfig(level=logging.DEBUG)

    unittest.main()

