import os

from setuptools import find_packages
from setuptools import setup


def parse_requirements_txt():
    root = os.path.dirname(os.path.abspath(__file__))
    requirements = []
    with open(os.path.join(root, 'requirements.txt'), 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
    return requirements


setup(
    name='collector',
    version='0.0.1',
    description="Service of collecting anonymous statistics",
    long_description="""Service of collecting anonymous statistics""",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Mirantis Inc.',
    author_email='product@mirantis.com',
    url='https://mirantis.com',
    keywords='fuel anonymous statistics collector mirantis',
    packages=find_packages(),
    zip_safe=False,
    install_requires=parse_requirements_txt(),
    include_package_data=True,
    scripts=['manage_collector.py'],
    # entry_points={
    #     'console_scripts': [
    #         'upgrade_db = collector.cli:main']
    # }
)
