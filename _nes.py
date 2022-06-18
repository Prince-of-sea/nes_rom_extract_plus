#!/usr/bin/env python3

def convert(p, l):
	with open(p, 'rb') as f:
		s = f.read()

	target = b'\x4E\x45\x53'#nesヘッダ
	target2 = b'\x4E\x45\x53\x1A'#(本来の)nesヘッダ - 一部WiiU抽出ROMで最後が\x00だったりするので

	idx = s.find(target)

	if ('-r' in l):
		rom = s[idx:]
	else:
		idx_5 = int(str(s[idx+4]))
		idx_6 = int(str(s[idx+5]))
		idx_end = idx+idx_5*16384+idx_6*8192+16 #16進で"(5番目のアドレス)×4000+(6番目のアドレス)×2000+10"
		rom = s[idx:idx_end]
	
	if not rom[0:4] == target2:#nesヘッダが正しくない場合修正
		rom = target2 + rom[4:]

	return(rom)

