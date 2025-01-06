import re
import shlex
import subprocess


def run_program():
    command = """
    curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json
    """
    cm = shlex.split(command)
    res = subprocess.run(cm, stderr=subprocess.STDOUT)
    print([(i, uid) for uid, i in enumerate(res.args, 1)])


if __name__ == "__main__":
    run_program()
