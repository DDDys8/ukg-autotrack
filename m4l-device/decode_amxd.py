import base64
import os

# 保存先ファイル名
output_path = "m4l-device/receive_osc_play_drum.amxd"

# Base64文字列（このあと提供）
base64_string = """
TVNDRgAAAAAAAACqAgAAAAAAABsAAAAUAAAAVGVzdCBNU0NHIENvbnRhaW5lcgAAAQAAAFoBAAAI
AAAB////AAACAAEAU2NvAAAAAAAAAAEAUgEAAP///wAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAFNQ
YXRjaGVyMAAAAAAAAAAAAENvdW50PTAKAAAAAAAAAA==  
"""


# デコードして保存
with open(output_path, "wb") as f:
    f.write(base64.b64decode(base64_string.strip()))

print("✅ .amxd file has been written to:", output_path)
