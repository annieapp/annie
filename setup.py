import setuptools

with open("requirements.txt", mode="r").readlines() as deps:
    for i, x in enumerate(deps):
        deps[i] = deps[i].replace("\n", "")

setuptools.setup(
    name='annie-server',
    version='0.0.1',
    author="Annie Team",
    description="Annie Server"
    license="See https://github.com/annieapp/annie/blob/master/LICENSE",
    url="https://annieapp.co",
    author_email="me@rdil.rocks",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=deps
)
