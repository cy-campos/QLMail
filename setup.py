from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: MacOS',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='QLMail',
    version='0.0.1',
    description='AWS Python Lambda Layer for Sending Emails via SES',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/cy-campos/QLMail',
    author='Christopher Campos',
    author_email='cy.campos1983@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='AWS Lambda SES Layer',
    packages=find_packages(),
    install_requires=['']
)
