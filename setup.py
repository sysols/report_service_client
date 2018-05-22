from setuptools import setup, find_packages


setup(
    name='report_service_client',
    version='0.1',
    packages=['report_service_client'],
    install_requires=['requests'],
    include_package_data=True,
    license='BSD 2-Clause License',
    description='A client for Report Service (by Maxim Afanasiev)',
    long_description=None,
    url='https://github.com/sysols/report_service_client',
    author='Alexey Tatarinov',
    author_email='a.tatarinov@sysolutions.ru',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 2-Clause License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
)
