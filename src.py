import os
from dotenv import load_dotenv

load_dotenv()


def named(num):
    if num > 10:
        print(os.environ['LLM'])


if __name__ == "__main__":
    named(11)