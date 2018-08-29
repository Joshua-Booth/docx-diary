import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(name='docx_diary',
                 version='1.0',
                 author="Joshua Booth",
                 author_email="me@joshuabooth.nz",
                 url="http://www.joshuabooth.nz/",
                 description="A command-line docx diary program",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 include_package_data=True)