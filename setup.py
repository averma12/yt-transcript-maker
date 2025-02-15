from setuptools import setup, find_packages

setup(
    name="yt-transcript-maker",
    version="0.1.0",
    author="Abhinav Verma",
    description="A tool to create timestamped transcripts from YouTube videos",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "yt-dlp",
        "pydub",
        "requests"
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)