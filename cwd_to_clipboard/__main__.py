import os
import pyperclip

spam = pyperclip.paste()


def main():
    """Run main CLI command."""
    cwd = os.getcwd()
    print(f"Copying current working directory to clipboard:\n >> {cwd}")
    pyperclip.copy(cwd)
    print(f"done!")


# Uncomment to debug
# if __name__ == "__main__":
#     main()
