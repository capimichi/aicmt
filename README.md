# AICMT - Automatic Commit via Artificial Intelligence

## What is

AICMT is a tool that automates the process of generating commit messages using artificial intelligence. It leverages models like GPT-4 to analyze code changes and generate meaningful commit messages, saving developers time and ensuring consistency.

## Installation

Install AICMT using pip:
```sh
pip install git+https://github.com/capimichi/aicmt.git
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

### Save configurations

You can export the configurations in the session with the export command:
```sh
export AICMT_MODEL=gpt-4o
```

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
