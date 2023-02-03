import os
from pathlib import Path

messages = []

def set_action_output(name: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as myfile:
        myfile.write(f"{name}={value}\n")

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
        for p in Path("").iterdir():
            files.append(p.name)
        all_files = ",".join(files)
        log_message(f"FILES_LISTING_1='{all_files}'")

        log_message("MY_VAR1=foo")
        log_message("MY_VAR2=bar")
        log_message("MY_VAR3=baz")

        fs = []
        for root, dirs, files in os.walk(""):
            for file in files:
                fs.append(str(file))

        xx = ",".join(fs)
        set_action_output("files", xx)
        set_action_output("the_files", files)

        x = []
        x.append("a")     
        x.append("b")     
        x.append("c")     
        set_action_output("x", x)


    except Exception as e:
        log_message("ERROR=Error")
    finally:
        send_log()


if __name__ == "__main__":
    main()
