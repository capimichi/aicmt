import click
import sys

from aicmt.aicmt import execute

def display_help():
    print("Usage: {} [options]".format(sys.argv[0]))
    print("\nOptions:")
    print("-h, --help    Show this help message")
    print("\nEnvironment Variables:")
    print("AICMT_MODEL          Model to use (default: gpt-4o-mini)")
    print("AICMT_SOURCE_TYPE    Source type to use (default: openai)")
    print("AICMT_API_BASE_URL   API base URL to use (default: https://api.openai.com/v1)")
    print("AICMT_DIFF_MAX_LENGTH Max length for diff (default: 500)")
    print("AICMT_API_KEY        API key to use")

@click.command()
@click.option('--help', is_flag=True, help='Show this help message')
def cli(help = False):
    """
    AICMT - Automatic commit via artificial intelligence
    """
    if help:
        display_help()
    else:
        execute()

if __name__ == '__main__':
    cli()