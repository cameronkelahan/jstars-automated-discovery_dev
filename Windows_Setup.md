Windows Setup Help
================

[![Formatted with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Linted with pylint](https://img.shields.io/badge/linting-pylint-green)](https://github.com/PyCQA/pylint)


This guide lays out the steps you must take if using a Windows OS computer.

----

## Setup

First, create a virtual environment called jst for this project.
```bash
python3 -m venv jst
```

Next, activate the environment with the following command
```bash
jst\Scripts\activate
```

Finally, install the required libraries using the supplied requirements_windows.txt.
```bash
pip install -r requirements_windows.txt
```
Windows requires a different version of torch and torchvision than what is written in the requirements.txt file that can be used for Linux.

Please reference this file for any errors/issues/troubleshooting that may come up as you move forward.
You may now return to the README file and continue following the instructions.

----

## Torch and CUDA issues

When running the 2nd given command in the 'Sample Pipeline' section of the README (with --inference), if CUDA is not installed on your machine with the correct
version of torch, torchvisiion, and torchaudio, it may throw a RuntimeError because because 'torch.cuda.is_available() is False.'

Please ensure CUDA is installed; you can follow this guide: https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#windows.

Once it is all installed, restart any IDE software you may be using and try running the --inference code again.

If the error persists, the version of torch you currently hace installed may be interfering with the CUDA. Below is a solution that worked for the developer when
modifying this tool to run on Windows:

To ensure you have the correct version of torch for your CUDA version, first uninstall torch, torchvision, and torchaudio (if present) by running this command:

```bash
pip uninstall torch torchvision torchaudio
```

Then, please go to https://pytorch.org/get-started/locally/ and select the desired PyTorch build (most recent stable one will be offered), your OS,
the package installation method (pip suggested), the language, and the correct CUDA version you have installed. Then, copy the given command and run it. This will
install a version of torch, torchvision, and torch audio that work with the CUDA version installed on your machine.

If issues persist, continue playing around with versions of CUDA and torch, following the CUDA intallation guide precisely.
