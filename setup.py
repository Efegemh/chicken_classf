import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.1'

REPO_NAME = 'chicken_classf'
AUTHOR_USER_NAME = 'Efegemh'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'emailexample@example.com'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app",
    long_description = long_description,
    long_description_content = 'text/markdown',
    url = f'https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues',
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)