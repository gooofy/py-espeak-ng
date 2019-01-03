#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

    def test_say_unkown_voice(self):

        esng = ESpeakNG(voice='unknown-voice')
        esng.pitch = 32
        esng.speed = 150
        res = esng.say('Hello World!', sync=True)

        self.assertNotEqual (res, [])


    def test_say_en(self):

        esng = ESpeakNG(voice='english-us')
        esng.pitch = 32
        esng.speed = 150
        res = esng.say('Hello World!', sync=True)

        self.assertEqual (res, [])

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

