# Copyright (c) 2016-2018 Braintech Sp. z o.o. [Ltd.] <http://www.braintech.pl>
# All rights reserved.
from setuptools import setup, find_packages

import versioneer


INSTALL_REQUIREMENTS = {
    'setup': [
    ],
    'install': [
        'numpy==1.17.2',
    ],
}

if __name__ == '__main__':
    setup(
        name='fuw_chatbot',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='example gitlab CI project',
        zip_safe=False,
        author='FUW',
        author_email='marian.dovgialo@fuw.edu.pl',
        license='Other/Proprietary License',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Topic :: Scientific/Engineering',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
        ],
        keywords='bci eeg obci',
        packages=find_packages(include=['fuw_chatbot']),
        include_package_data=True,
        setup_requires=INSTALL_REQUIREMENTS['setup'],
        install_requires=INSTALL_REQUIREMENTS['install'],
        extras_require=INSTALL_REQUIREMENTS,
        entry_points={
            'console_scripts': [],
        },
        ext_modules=[],
    )
