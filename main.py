import sys
from servers import get_status_label

if len(sys.argv) < 2:
    print(f'Usage: python main.py <status>')
    sys.exit(1)
else:
    print(get_status_label(sys.argv[1]))
