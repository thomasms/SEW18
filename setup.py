from setuptools import setup


setup(name='setup',
      version='0.0.1',
      description='A dummy package for SEW18',
      url='https://github.com/thomasms/SEW18',
      author='UKAEA',
      author_email='stainer.tom@gmail.com',
      license='GNU General Public License v3.0',
      packages=[
            'sewpy'
      ],
      install_requires=[],
      python_requires='>=3',
      setup_requires=['pytest-runner'],
      test_suite='tests.testsuite',
      tests_require=['pytest-cov'],
      zip_safe=False)
