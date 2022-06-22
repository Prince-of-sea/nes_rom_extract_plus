#!/usr/bin/env python3
import struct

def QD2FDS_py(disk):
	#ここに 変換前バイナリ(.qd)→変換後バイナリ(.fds - 64KBヘッダなし)を書く
	# 参考元 - https://gist.github.com/einstein95/6545066905680466cdf200c4cc8ca4f0

	disk = bytearray(disk)
	del disk[0x38:0x3A]  # 01 block chksum

	# fn = disk[0x39]  # get num of files from 02 block
	pos = 0x3A

	del disk[pos: pos + 2]  # 02 block chksum

	try:
		while disk[pos] == 3:  # if there's any more files, like in Doki Doki Panic
			filesize, = struct.unpack('<H', disk[pos + 0xD: pos + 0xF])

			del disk[pos + 0x10: pos + 0x12]  # 03 block chksum

			pos = pos + 0x10 + 1 + filesize

			del disk[pos: pos + 2]  # 04 block chksum

	except IndexError:
		pass

	if len(disk) > 65500:
		disk = disk[:65500]
	else:
		disk = disk.ljust(65500, b"\0")
	return disk


def convert(p, l):
	target = b'*NINTENDO-HVC*'
	rom_tmp = b''
	i = 0

	with open(p, 'rb') as f:
		s = f.read()
	idx = s.find(target)
	rom_head = (idx - 1)

	while(True):
		d = s[rom_head+(65536*i):rom_head+(65536*(i+1))]
		if not (d[1:15] == target):
			break

		rom_tmp += QD2FDS_py(d)
		i += 1

	if ('-nh' in l):
		rom = rom_tmp
	else:
		fds = b'\x46\x44\x53\x1A' + int(hex(i), 16).to_bytes(12, byteorder='little')# Disk枚数→16進
		rom = fds + rom_tmp

	return rom