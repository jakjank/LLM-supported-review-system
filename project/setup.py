from setuptools import setup, find_packages

setup(
    name='project',  # The name of package
    version='0.1',
    packages=find_packages(where='src'),  # Automatically find and include all packages
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'run_prompt_1=project.prompt1:main',  # Define console script entry point
        ],
    },
)
