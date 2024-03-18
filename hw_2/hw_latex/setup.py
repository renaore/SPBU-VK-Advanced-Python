from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='latex_table_image',
  version='0.0.1',
  author='renaore',
  author_email='lolrenchik@gmail.com',
  description='This is the simplest module for creating latex code for tables and images.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  # url='https://github.com/renaore/python_adv/tree/main/hw_2',
  url = ' https://upload.pypi.org/legacy/',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='latex ',
  project_urls={
    'GitHub': 'https://github.com/renaore/python_adv'
  },
  python_requires='>=3.9'
)
