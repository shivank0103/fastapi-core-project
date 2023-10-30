import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='cashifycore',
    version='0.0.1',
    description='Core for Fast API projects',
    url='https://github.com/saket-cashify/cashify-core-python-fastapi',
    author='Shivank',
    author_email='shivank0103@gmail.com',
    license='unlicense',
    # packages=['cashifycore'],
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[
        'cashifypythoncachingframework @ git+ssh://git@cashifycache/reglobe/cashify-python-caching.git',
        'cashifypythonetcd @ git+ssh://git@cashifyetcd/reglobe/cashify-python-etcd.git',
        'cashifypythonrestclient @ git+ssh://git@cashifyrestclient/reglobe/cashify-python-rest-client.git',
        'cashifypythonlogger @ git+ssh://git@cashifylogger/reglobe/cashify-python-logger.git',
        'mysql-connector==2.2.9',
        'PyJWT==2.5.0'
    ],
    zip_safe=False
)
