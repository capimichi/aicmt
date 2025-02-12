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
- `AICMT_API_TIMEOUT`: Timeout for API requests in seconds (default: `10`)

> For the base url, when source type is `openai`, you can select any Openai compatible API, like OpenRouter, Deepseek, ecc.

### Save configurations

You can export the configurations in the session with the export command:
```sh
export AICMT_MODEL=gpt-4o
```

### Sample Configurations

#### OpenAI
```sh
export AICMT_MODEL="gpt-4o-mini"
export AICMT_SOURCE_TYPE="openai"
export AICMT_API_BASE_URL="https://api.openai.com/v1"
export AICMT_API_KEY="your_openai_api_key"
```

#### Ollama
```sh
export AICMT_MODEL="llama3:8b"
export AICMT_SOURCE_TYPE="ollama"
export AICMT_API_BASE_URL="http://localhost:11434"
```

#### OpenRouter
```sh
export AICMT_MODEL="gpt-4o-mini"
export AICMT_SOURCE_TYPE="openai"
export AICMT_API_BASE_URL="https://openrouter.ai/api/v1"
export AICMT_API_KEY="your_openrouter_api_key"
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
