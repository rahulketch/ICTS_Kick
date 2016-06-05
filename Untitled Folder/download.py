f = open('download.sh','w')



["%04d" % x for x in range(10000)]

for x in range(150,209):
	f.write('wget -o {}.log -O {}.tgz \"http://www.black-holes.org/waveforms/data/Download.php?id=SXS:BBH:{}\";\n'.format("%04d"%x,"%04d"%x,"%04d"%x))
f.close()
