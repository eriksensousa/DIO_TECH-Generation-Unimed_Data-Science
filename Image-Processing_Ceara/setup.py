from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Image-Processing_Ceara",
    version="0.0.1",
    author="Iago Magalhães",
    author_email="iagomagalhaes23@gmail.com",
    description="Projeto com comandos inspirados no português cearense",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IagoMagalhaes23/Geracao-Tech-Unimed-BH_Ciencia-de-Dados",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)