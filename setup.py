import platform
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Build extras_requires based on platform
def build_additional_requires():
    # py_version = platform.python_version()[0:3].replace('.', "")
    # if platform.system() == "Linux" and platform.machine() == "x86_64":
    #     additional_requires=[
    #         f"speexdsp_ns @ https://github.com/dscripka/openWakeWord/releases/download/v0.1.1/speexdsp_ns-0.1.2-cp{py_version}-cp{py_version}-linux_x86_64.whl",
    #     ]
    # elif platform.system() == "Linux" and platform.machine() == "aarch64":
    #     additional_requires=[
    #         f"speexdsp_ns @ https://github.com/dscripka/openWakeWord/releases/download/v0.1.1/speexdsp_ns-0.1.2-cp{py_version}-cp{py_version}-linux_aarch64.whl",
    #     ],
    if platform.system() == "Windows" and platform.machine() == "x86_64":
        additional_requires = [
            'PyAudioWPatch'
        ]
    else:
        additional_requires = []

    return additional_requires


setuptools.setup(
    name="openwakeword",
    version="0.6.0",
    install_requires=[
        'onnxruntime>=1.23.2',
        'ai-edge-litert>=2.0.3; platform_system == "Linux" or platform_system == "Darwin"',
        'speexdsp-ns>=0.1.2; platform_system == "Linux"',
        'tqdm>=4.67.1',
        'scipy>=1.16.3',
        'scikit-learn>=1.7.2',
        'requests>=2.32.5',
    ],
    extras_require={
        'test': [
                    'pytest>=9.0.0',
                    'pytest-cov>=7.0.0',
                    'pytest-flake8>=1.3.0',
                    'flake8>=7.3.0',
                    'pytest-mypy>=1.0.1',
                    'types-requests>=2.32.4.20250913',
                    'types-PyYAML>=6.0.12.20250915',
                    'mock>=5.2.0',
                    'types-mock>=5.2.0.20250924',
                ],
        'full': [
                    'mutagen>=1.47.0',
                    'torch>=2.9.0',
                    'torchaudio>=2.9.0',
                    'torchinfo>=1.8.0',
                    'torchmetrics>=1.8.2',
                    'speechbrain>=1.0.3',
                    'audiomentations>=0.43.1',
                    'torch-audiomentations>=0.12.0',
                    'tqdm>=4.67.1',
                    'pytest>=9.0.0',
                    'pytest-cov>=7.0.0',
                    'pytest-flake8>=1.3.0',
                    'pytest-mypy>=1.0.1',
                    'acoustics>=0.2.6',
                    'pyyaml>=6.0.3',
                    'tensorflow-cpu>=2.20.0',
                    'tensorflow-probability>=0.25.0',
                    'protobuf>=6.33.0',
                    'onnx>=1.19.1',
                    'pronouncing>=0.2.0',
                    'datasets>=4.4.1',
                    'deep-phonemizer>=0.0.19',
                    'piper-tts>=1.3.0'
                ]
    },
    author="David Scripka",
    author_email="david.scripka@gmail.com",
    description="An open-source audio wake word (or phrase) detection framework with a focus on performance and simplicity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/openwakeword",
    project_urls={
        "Bug Tracker": "https://pypi.org/project/openwakeword/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
)