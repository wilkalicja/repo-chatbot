from setuptools import setup, find_packages

import versioneer


INSTALL_REQUIREMENTS = {
    'setup': [
    ],
    'install': [
        'numpy==1.22.3',
    ],
}

if __name__ == '__main__':
    setup(
        name='fuw_chatbot',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='FUW Chatbot',
        zip_safe=False,
        author='',
        author_email='',
        license='Other/Proprietary License',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Topic :: Scientific/Engineering',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
        ],
        keywords='fuw chatbot',
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
