

def QD2FDS_py(d, i):
	#ここに 変換前バイナリ(.qd)→変換後バイナリ(.fds - 64KBヘッダなし)を書く



	#---------------------------以下テスト用----------------------------
	Program = r'Program.exe'
	
	with open('__disk'+str(i)+'.qd', 'wb') as f:
		f.write(d)

	subprocess.run([Program, '__disk'+str(i)+'.qd'], shell=True)

	with open('__disk'+str(i)+'.fds', 'rb') as f:
		c = f.read()
	
	return c[0:65536-36]#64KBじゃない場合の保険 - キレイにできてれば[0:65536-36]は消していい


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

		rom += QD2FDS_py(d, i)
		i += 1

	if i == 1:
		fds = b'\x46\x44\x53\x1A\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk1枚組
	elif i == 2:
		fds = b'\x46\x44\x53\x1A\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk2枚組
	elif i == 4:
		fds = b'\x46\x44\x53\x1A\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'# Disk2x2枚組

	rom = fds + rom
	return rom


#---------------------------以下もテスト用----------------------------
if __name__ == "__main__":
	import subprocess

	input = r"main.dol"
	output = r"x.fds"
	args = []

	with open(output, 'wb') as f:
		f.write(convert(input, args))