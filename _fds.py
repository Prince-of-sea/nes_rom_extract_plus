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
	target = b'\x01\x2A\x4E\x49\x4E\x54\x45\x4E\x44\x4F\x2D\x48\x56\x43\x2A\x01'# " *NINTENDO-HVC* "
	rom = b''
	i = 0

	with open(p, 'rb') as f:
		s = f.read()
	idx = s.find(target)

	while(True):
		d = s[idx+(64*1024*i):idx+(64*1024*(i+1))]
		if not (d[0:16] == target):
			break

		rom += QD2FDS_py(d)
		i += 1

	if i == 1:
		fds = b'\x46\x44\x53\x1A\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk1枚組
	elif i == 2:
		fds = b'\x46\x44\x53\x1A\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk2枚組
	elif i == 4:
		fds = b'\x46\x44\x53\x1A\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk2x2枚組

	rom = fds + rom
	return rom