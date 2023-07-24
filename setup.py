from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="vonage_sms_api",
    version="1.0",
    description="A simplified sms API wrapper for vonage/nexmo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahaafarooq/vonage-sms-api",
    download_url="",
    author="Tahaa Farooq",
    author_email="tahacodez@gmail.com",
    license="MIT",
    packages=["vonage_sms_api"],
    keywords=[
        "Vonage SMS API",
        "Vonage" "Nexmo" "SMS" "sms api" "API" "Programming API" "SMS wrapper",
        "python-tanzania",
    ],
    install_requires=["vonage", "requests", "python-dotenv"],
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers"
        "Topic :: SMS API Wrapper :: API",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)