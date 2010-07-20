try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Exceptable',
    version='0.1.0',
    description='DB Exception Management',
    long_description="""
    What is Exceptable?
    ===================
    Exceptable is a library that handles matching formatted exceptions raised
    in PostgreSQL to Python exception types, allowing for a simple and easy
    process for the database to throw a named exception in Python.
    """,
    author='Aurynn Shaw, Commandprompt, Inc.',
    author_email='ashaw@commandprompt.com',
    url='https://public.commandprompt.com/projects/exceptable/wiki',
    download_url='https://projects.commandprompt.com/public/exceptable/repo/dist/Exceptable-0.1.0.tar.gz',
    # install_requires=[
    # ],
    packages=find_packages(),
    test_suite='nose.collector',
    license='LGPL',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Topic :: Software Development",
    ],
#    data_files=[
#        ('sql/', ['sql/*.sql'])
#    ],
)

