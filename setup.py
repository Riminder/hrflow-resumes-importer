from setuptools import setup

setup(name='hrflow_resume_importer',
      version='0.0.4',
      description='Hrflow resume importer.',
      url='https://github.com/Riminder/hrflow-resumes-importer',
      author='riminder',
      author_email='contact@hrflow.ai',
      license='MIT',
      install_requires=[
          'hrflow'
      ],
      packages=['resume_importer'],
      entry_points={
        'console_scripts': [
            'resumeImporter = resume_importer.resume_importer:main',
        ]
      },
      python_requires='>=3.5',
      zip_safe=False)
