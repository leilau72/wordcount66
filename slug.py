import re, sys

def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or 'x'

if __name__ == '__main__':
    print(slug(' '.join(sys.argv[1:]) or 'hello world'))
