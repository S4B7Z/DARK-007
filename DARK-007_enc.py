# Compiled By DARK-SHADOW
# Github :  https://github.com/s4b7z

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))