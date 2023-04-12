#!/usr/bin/env python3
import os
from os import path

from setuptools import setup

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


def get_version():
    """ Find the version of ovos-core"""
    version = None
    version_file = os.path.join(BASE_PATH, 'ovos_audio_gender_classifier', 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if int(alpha):
        version += f"a{alpha}"
    return version


PLUGIN_ENTRY_POINT = 'ovos-audio-classifier-gender=ovos_audio_gender_classifier:SpeakerGenderClassifier'
setup(
    name='ovos-audio-classifier-gender',
    version=get_version(),
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
