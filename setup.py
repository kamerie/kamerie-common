from setuptools import setup, find_packages

setup(
    name='kamerie_common',
    version='0.1',
    author='Chen Asraf & Dor Munis',
    url='https://github.com/kamerie/kamerie-common',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    platforms='any',
    license='Apache 2.0',
    install_requires=['pika', 'pymongo'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
