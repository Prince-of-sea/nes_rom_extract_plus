#!/usr/bin/env python3

def convert(p, l):
	with open(p, 'rb') as f:
		s = f.read()
	
	d = {
		# 参考 - https://www.reddit.com/r/emulation/comments/377gug
		'0x239':b'\x85',
		'0x406':b'\x85',
		'0x73e':b'\xA2',
		'0x73f':b'\xB2',
		'0x740':b'\xCA',
		'0x7a4':b'\x4C',
		'0xef4':b'\xA5',
	}

	target = b'*CVH-ODNETNIN*'
	idx = s.find(target)
	rom_head = ( idx - int('6D5', 16) )
	rom_tmp = s[rom_head:rom_head+8192]

	if ('-nf' in l):
		rom = rom_tmp
	else:
		rom = b''
		for i, b in enumerate(rom_tmp):
			getbin = d.get(hex(i).lower())
			rom += getbin if bool(getbin) else bytes([b])

	return rom