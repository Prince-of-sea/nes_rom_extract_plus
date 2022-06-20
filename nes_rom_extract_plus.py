#!/usr/bin/env python3
import sys
import os

import _nes
import _fds
import _bios


def Error_mode(msg):
	print('Error!:' + msg)
	sys.exit(1)


try:
	args = sys.argv[1:-2]
	input = sys.argv[-2]
	output = sys.argv[-1]
except:
	Error_mode('引数が不正です。')

input_ext = (os.path.splitext(input)[1]).lower()
output_ext = (os.path.splitext(output)[1]).lower()

if not os.path.exists(input):
	Error_mode('"' + input + '"は存在しません')

with open(output, 'wb') as f:
	if output_ext == '.nes':
		f.write(_nes.convert(input, args))
	elif output_ext == '.fds':
		f.write(_fds.convert(input, args))
	elif output_ext == '.rom':
		f.write(_bios.convert(input, args))
	#elif output_ext == '.snes':
		#f.write(_snes.convert(input, args))
	else:
		Error_mode('出力時の拡張子が非対応です。')
