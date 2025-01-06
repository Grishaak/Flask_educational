import subprocess
import time


def run_popen():
    p = subprocess.Popen(['python', 'test_sub.py'])
    return p


if __name__ == "__main__":
    res = run_popen()
