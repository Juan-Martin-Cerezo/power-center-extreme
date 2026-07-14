import re

with open('/home/juan/power-center/power-center.py', 'r') as f:
    content = f.read()

# Replace subprocess.run(..., shell=True)
content = re.sub(
    r'(subprocess\.run\(.*?, shell=True)(\))',
    r'\1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL\2',
    content
)

# Replace subprocess.Popen(..., shell=True)
content = re.sub(
    r'(subprocess\.Popen\(.*?, shell=True)(\))',
    r'\1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL\2',
    content
)

with open('/home/juan/power-center/power-center.py', 'w') as f:
    f.write(content)
