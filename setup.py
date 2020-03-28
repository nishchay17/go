import setuptools

with open("README.md", "r") as readMe:
    long_description = readMe.read()

setuptools.setup(
    name = 'go',
    version = '0.1.0',
    scripts = ['go'] ,
    author = "Nishchay Trivedi",
    author_email = "nishchay13971@gmail.com",
    description = "A dir utility package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'go = go.__main__:main'
        ]
    }
)
