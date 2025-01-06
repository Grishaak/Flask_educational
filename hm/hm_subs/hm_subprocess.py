import shlex
import subprocess
from typing import Tuple


def run_sub_code(code: str, timeout: int):
    command = f"python -c {code}"
    command = shlex.split(command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    killed = False
    try:
        out, errs = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        out, errs = process.communicate()
        killed = True
    return out.decode(), errs.decode(), killed


if __name__ == "__main__":
    output, _, _ = run_sub_code("print(type('1111'))", 4)
