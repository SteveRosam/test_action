import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'FOO=BAR', file=fh)


if __name__ == "__main__":
    main()
