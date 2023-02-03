import os

messages = []

def send_log():
    env_file = os.getenv('GITHUB_ENV')
    env_file = "./foo.txt"
    message = "\n".join(messages)

    with open(env_file, "a") as myfile:
        myfile.write(f"{message}")

def log_message(message):
    messages.append(message)


def main():
    try:
        log_message("\nMY_VAR=foo")
        log_message("\nMY_VAR=bar")
        log_message("\nMY_VAR=baz")
    except Exception as e:
        log_message("\nMY_VAR=Error")
    finally:
        send_log()


if __name__ == "__main__":
    main()
