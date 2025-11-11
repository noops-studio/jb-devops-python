import subprocess


result = subprocess.run('echoa Hello, World!', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    



# result = run_command("eecho Hello, World!")

if result.returncode == 0:
    print("Command Output:", result.stdout)
else:
    print(result.stderr)