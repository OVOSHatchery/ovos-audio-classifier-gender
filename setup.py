#!/usr/bin/env python3
from setuptools import setup
from os import path, getenv
import os


BASE_PATH = os.path.abspath(path.dirname(__file__))


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASE_PATH, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        if 'MYCROFT_LOOSE_REQUIREMENTS' in os.environ:
            print('USING LOOSE REQUIREMENTS!')
            requirements = [r.replace('==', '>=').replace('~=', '>=') for r in requirements]
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]




PLUGIN_ENTRY_POINT = 'ovos-audio-classifier-gender=ovos_audio_gender_classifier:SpeakerGenderClassifier'
setup(
    name='ovos-audio-classifier-gender',
    version='0.0.1',
    description='A audio parser/classifier/transformer plugin for OVOS',
    url='https://github.com/OpenVoiceOS/ovos-audio-classifier-gender',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    install_requires=required("requirements.txt"),
    license='bsd3',
    packages=['ovos_audio_gender_classifier'],
    zip_safe=True,
    keywords='OVOS plugin audio parser/classifier/transformer',
    entry_points={'neon.plugin.audio': PLUGIN_ENTRY_POINT}
)
