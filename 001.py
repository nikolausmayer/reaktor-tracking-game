
import base64

raw = open('001-signal.txt').read()

## 16-Byte chunks
for start in range(len(raw)-16):
    sub = raw[start:start+16]
    assert(len(sub) == 16)
    ## Check for duplicate characters in chunk
    if len(set(sub)) == 16:
        print(base64.b64decode(sub).decode())

