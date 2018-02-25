from setuptools import setup

setup(name='editorconfig_git_preserve_history',
      version='0.1',
      description='Commit changes to editorconfig and preserve authorship',
      url='http://github.com/dmeybohm/editorconfig-git-preserve-history',
      author='David Meybohm',
      author_email='dmeybohm@gmail.com',
      license='MIT',
      packages=['editorconfig_git_preserve_history'],
      install_requires=[
          'EditorConfig>=0.12.1',
      ],
      test_suite = 'nose.collector',
      tests_require = ['nose'])