import os
import requests  # noqa We are just importing this to prove the dependency installed correctly

messages = []

def send_log():
    env_file = os.getenv('GITHUB_ENV')

    message = "\n".join(messages)

    with open(env_file, "a") as myfile:
        myfile.write(f"MY_VAR={message}")

def log_message(message):
    messages.append(message)


def main():
    try:
        log_message("foo")
        log_message("bar")
        log_message("baz")
    except Exception as e:
        log_message("Error")
    finally:
        send_log()


if __name__ == "__main__":
    main()
