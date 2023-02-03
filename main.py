import os
from pathlib import Path

messages = []

def send_log():
    env_file = os.getenv('GITHUB_ENV')
    #env_file = "./foo.txt"
    message = "\n".join(messages)

    with open(env_file, "a") as myfile:
        myfile.write(f"{message}")

def log_message(message):
    messages.append(message)


def main():

    try:
        files = []
        for p in Path("./").iterdir():
            files.append(p.name)
        all_files = ",".join(files)
        log_message(f"FILES_LISTING_1={all_files}")

        log_message("MY_VAR1=foo")
        log_message("MY_VAR2=bar")
        log_message("MY_VAR3=baz")
    except Exception as e:
        log_message("ERROR=Error")
    finally:
        send_log()


if __name__ == "__main__":
    main()
