

def QD2FDS_py(d):
	#ここに 変換前バイナリ(.qd)→変換後バイナリ(.fds - 64KBヘッダなし)を書く


	#! 参考元
	#! http://www.neko.ne.jp/~freewing/hardware/nintendo_format_converter_qd_to_fds/
	with open(d, 'rb') as f:
		rbuff = f.read()
		wbuff = bytes(65500 * 2)
		wbuff = list(wbuff)

		rpos = 0
		wpos = 0
		fcnt = 0
		cpsize = 0
		size04 = 0
		while (rpos < len(rbuff)):
			rb = bytes([rbuff[rpos]])

			if (rb == b"\x01"):
				cpsize = b"\x38"
			elif (rb == b"\x02"):
				cpsize = b"\x02"
				fcnt = rbuff[rpos + 1]
			elif (rb == b"\x03"):
				cpsize = b"\x10"
				size04 = (rbuff[rpos + 14] << 8) + rbuff[rpos + 13]
			elif (rb == b"\x04"):
				cpsize = size04 + 1
				if (fcnt > 0):
					fcnt -= 1
				else:
					exit(1)
			elif (rb == b"\x00"):
				if (fcnt == 0):
					cpsize = b"0x10000" - (rpos & 0xffff)
				else:
					exit(1)


			while (cpsize > b"\x00") and (wpos < len(wbuff)):
				wpos += 1
				rpos += 1
				try:
					wbuff[wpos] = rbuff[rpos]
				except:
					pass
			
			if (rb == b"\x00"):
				if (wpos < b"0x10000"):
					wpos = b"0xFFDC"
			else:
				rpos += 2

	return bytes(wbuff)[0:65500]


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