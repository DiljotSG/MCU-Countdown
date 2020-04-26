# Setup

This codebase uses Python3.7.X/Python3.8.X. These setup instructions are for macOS using [Homebrew](https://brew.sh).
Installing these dependencies should be similar for other platforms with the appropriate package managers for that platform.

## Python3 Installation

1. Install python.

    ```shell
    brew install python
    sudo pip3 install virtualenv
    ```

## Environment Setup

These steps are required for development.

1. Create a Python virtual environment.

    ```shell
    virtualenv -p python3 venv
    ```

2. Activate the environment.

    ```shell
    . venv/bin/activate
    ```

3. Install Python dependencies.

    ```shell
    pip3 install -r dev-requirements.txt
    pip3 install -r requirements.txt
    ```

4. Run the application locally.

    ```shell
    python3 handler.py
    ```
