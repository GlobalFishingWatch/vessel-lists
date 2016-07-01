from setuptools import setup
from setuptools import find_packages


setup(
  name = 'treniformis',
  packages = find_packages(), 
  include_package_data = True,
  package_data = {
    'treniformis': ['known-fishing/known-fishing-v1/*',
                    'classification_lists/*.csv', 'classification_lists/*.md',
                    'classification_results/*.csv', 'classification_lists/*.md',
                    'exported/*/*'
                   ],
  },
  version = '0.1',
  description = '',
  author = 'Global Fishing Watch',
  author_email = 'info@GlobalFishingWatch.org',
  url = 'https://github.com/GlobalFishingWatch/vessel-lists',
)