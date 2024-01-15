from setuptools import setup, find_packages
#
print(find_packages("src"))
setup(
    name='rrprettier',
    version='0.1',
    packages=find_packages(),
    # install_requires=[
    #     "requests>=2.31.0"
    #     # List any dependencies your library may have
    # ],
    package_dir={"":"src"}
    #long_description="to prettify data",
    #long_description_content_type="text/markdown"
)