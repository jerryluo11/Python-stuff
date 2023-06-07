from pathlib import Path

# Absolute path
# /usr/local/bin
# Relative path

path = Path()
for file in path.glob('*.py'):
    print(file)