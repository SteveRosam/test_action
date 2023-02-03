import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    env_file = os.getenv('GITHUB_ENV')

    with open(env_file, "a") as myfile:
        myfile.write("MY_VAR=MY_VALUE")

    with open(env_file, "a") as myfile:
        myfile.write("\nMY_VAR=MY_VALUE2")


if __name__ == "__main__":
    main()
