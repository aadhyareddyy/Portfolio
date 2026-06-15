import sys
import re

def clean_vtt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    clean = []
    for line in lines:
        line = line.strip()
        if '-->' in line:
            continue
        if line.isdigit():
            continue
        if 'WEBVTT' in line:
            continue
        if line == '':
            continue
        line = re.sub(r'<[^>]+>', '', line)
        clean.append(line)
    return ' '.join(clean)

if __name__ == '__main__':
    filepath = sys.argv[1]
    result = clean_vtt(filepath)
    output_path = filepath.replace('.vtt', '_clean.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Saved to {output_path}")
