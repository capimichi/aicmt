# AICMT - Automatic Commit via Artificial Intelligence

## What is

AICMT is a tool that automates the process of generating commit messages using artificial intelligence. It leverages models like GPT-4 to analyze code changes and generate meaningful commit messages, saving developers time and ensuring consistency.

## Installation

### Ubuntu

1. Clone the repository:
    ```sh
    git clone https://github.com/capimichi/aicmt.git
    cd aicmt
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Mac

1. Clone the repository:
    ```sh
    git clone https://github.com/capimichi/aicmt.git
    cd aicmt
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Windows

1. Clone the repository:
    ```sh
    git clone https://github.com/capimichi/aicmt.git
    cd aicmt
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use AICMT, simply run the following command in your terminal:
```sh
aicmt
```

This will analyze your git status and generate commit messages for the changes.

## Configurations

AICMT can be configured using environment variables:

- `AICMT_MODEL`: Model to use (default: `gpt-4o-mini`)
- `AICMT_SOURCE_TYPE`: Source type to use (default: `openai`)
- `AICMT_API_BASE_URL`: API base URL to use (default: `https://api.openai.com/v1`)
- `AICMT_DIFF_MAX_LENGTH`: Max length for diff (default: `500`)
- `AICMT_API_KEY`: API key to use
- `AICMT_REMOVE_CHARS`: Characters to remove, separated by comma (default: '`,"'`)
- `AICMT_PROMPT_TEMPLATE`: Prompt template to use (default: see `aicmt.py`)

## Requirements

- Python 3.6+
- `certifi`
- `charset-normalizer`
- `click`
- `idna`
- `python-dotenv`
- `requests`
- `urllib3`

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
