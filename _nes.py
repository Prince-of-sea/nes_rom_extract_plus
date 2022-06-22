#!/usr/bin/env python3

def convert(p, l):
	with open(p, 'rb') as f:
		s = f.read()

	target = b'\x4E\x45\x53'#nesヘッダ
	idx = s.find(target)

	if ('-l' in l):
		rom = s[idx:]
	else:
		idx_5 = int(str(s[idx+4]))
		idx_6 = int(str(s[idx+5]))
		idx_end = idx+idx_5*16384+idx_6*8192+16 #16進で"(5番目のアドレス)×4000+(6番目のアドレス)×2000+10"
		rom = s[idx:idx_end]

	if (not '-nf' in l) and (not rom[3] == b'\x1A'):
		rom = target + b'\x1A' + rom[4:]
	
	return(rom)

