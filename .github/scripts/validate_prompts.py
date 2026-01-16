#!/usr/bin/env python3
import glob
import sys

def main():
    files = glob.glob('prompts/*.md')
    if not files:
        print('ERROR: no prompt files found in prompts/')
        sys.exit(1)
    errors = 0
    for path in files:
        with open(path, encoding='utf-8') as f:
            text = f.read()
        lines = [l for l in text.splitlines() if l.strip() and not l.strip().startswith('#')]
        if len(lines) < 8:
            print(f'ERROR: {path} has only {len(lines)} content lines (expected >=8)')
            errors += 1
    if errors:
        print('\nPrompt validation failed.')
        sys.exit(1)
    print('Prompt validation passed.')

if __name__ == '__main__':
    main()
