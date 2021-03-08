import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="administrative_dashboard",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "administrative_dashboard"},
    packages=setuptools.find_packages(where="administrative_dashboard"),

    install_requires=[
        "aws-cdk.core==1.72.0",
        "aws-cdk.aws_iam==1.72.0",
        "aws-cdk.aws_lambda==1.72.0",
        "aws-cdk.aws_events==1.72.0",
        "aws-cdk.aws_events_targets==1.72.0",
        "boto3",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
