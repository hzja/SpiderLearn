# 原创
：  【MP4 QuickTime隐写】tcsteg、jpegEOFx、detect anomalies in video files

# 【MP4 QuickTime隐写】tcsteg、jpegEOFx、detect anomalies in video files

**目录**

[一、TCSteg](#%E4%B8%80%E3%80%81TCSteg)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、现状：](#1.2%E3%80%81%E7%8E%B0%E7%8A%B6%EF%BC%9A)

[1.3、原理：](#1.3%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.4、检测：](#1.4%E3%80%81%E6%A3%80%E6%B5%8B%EF%BC%9A)

[二、脚本（源代码）](#%E4%BA%8C%E3%80%81%E8%84%9A%E6%9C%AC%EF%BC%88%E6%BA%90%E4%BB%A3%E7%A0%81%EF%BC%89)

[2.1、tcsteg2.py：](#2.1%E3%80%81tcsteg2.py%EF%BC%9A)

[2.2、jpegEOFx.py](#2.2%E3%80%81jpegEOFx.py)

[2.3、detect anomalies in video files.py](#2.3%E3%80%81detect%20anomalies%20in%20video%20files.py)

---


## 一、TCSteg

> 
<h2>1.1、简介：</h2>
TCSteg是个新式数据隐藏武器， 它在TrueCrypt（一个非常有名且好用的加密工具）的基础上又增加了隐写掩盖功能， 最新的一个进步可以把一个TrueCrypt容器隐藏到MP4或QuickTime多媒体文件中。
<hr/>
这个应用软件 tcsteg. py是一个纯python脚本， 并以略带限制的开源形式共享出来。 这个工具简单易懂，支待以QuickTime和MP4多媒体容器作为载体。
<hr/>
tcsteg.sy应用程序将TrueCrypt文件容器嵌入到了现有的MP4或QuickTime的多媒体 载体文件中， 这使得处理后的文件运行时既可以是一个标准的多媒体文件， 也可以是一个可挂载的TrueCrypt卷。


---


> 
<h3>1.2、现状：</h3>
使用 tcsteg. Py可以在不影响电影效果的情况下， 将TrueCrypt容器嵌入到QuickTim e或MP4电影中。 换句话说， 电影会照常播放， 虽然电影的大小因隐藏的容器而略有增 加，但通过常规的检查是检测不到的。 如果有人真想找到隐藏信息， 没有专业的检测技术， 要想发现其中嵌入的TrueCrypt容器是相当困难的。 甚至， 即使TrueCrypt被检测出来了， 没有用来加密隐藏的TrueCrypt卷的密钥， 要提取出具体的隐藏信息几乎是不可能的
<hr/>
网络上(YouTube等）快速增长的电影文件传输量，为秘密信息的隐藏和隐蔽传输提供 了丰富的土壤， 而且据预测， 在最近十年内， 还将以几何级数增长。 可想而知， 这个新方法可以被恋童癖者充分利用， 通过共享看似正常、 无伤大雅的数据媒体来交换他们想要的信息， 甚至还可能被不法分子用来进行大量的地下消息交换。


> 
<h3>1.3、原理：</h3>
可以看到一个典型的电影文件的简化结构（注意：是简化的，因为描述详细结构可能要写 本书）。 媒体数据(Media Data, MDAT)和采样表块偏移(S ampleTable Chunk Offset, STOC) 是多媒体文件用来隐藏数据的关键部分， MDAT中包含的是真正的原始视频， 即视频数据。MDAT数据块的长度大小不一，排列顺序也没有严格要求。 STCO是个索引表， 包含了指向MDAT中各数据块位置的指针。 STCO使得MDAT中的块可以以无序的状态存在

 
电影文件的基本结构
<hr/>
这种灵活性有很多优点：
快速编辑、 检索、 本地回放和视频流能力。只需要简单地修改STCO中的指针就可以方便快捷地调整样本顺序。 对文件的每次检索都需要访问STCO来查询MDAT块的正确位置， 播放电影时我们靠这种方法来定位电影的指定部分、 快进、 回放和记录曾经停止过的位置。 通过操作MDAT和STCO, tcsteg.py可以嵌入一个不包含原始音频或视频， 却含有TrueCrypt隐藏卷内容的数据块。
<hr/>

经tcsteg.py略微修改的电影文件结构， 为了让隐藏有效， TrueCrypt容器必须包含两个卷：外层卷和内层卷（隐藏卷）。为了进一步掩盖数据嵌入痕迹，嵌入数据的过程中会丢弃外层卷，但内层卷还是完整的。TCTSTEG还会加入一些伪造数据让MDAT看起来更加真实合法。因此，如果用十六进制编辑器来查看多媒体文件，那么你不会看到MDAT中有任何可疑数据。播放媒体文件时也不会有任何异常，但如果用TrueCrypt挂载媒体文件

被嵌入True Crypt容器的电影文件


---


<br/>  

> 
<h3>1.4、检测：</h3>
如果想要检查的话，通过编程手段就可以发现这个混合媒体(TruCrypt文件），这就涉及分析多媒体文件的STCO和MSAT部分了。
通过检查STCO中每个数据块偏移量，MDAT中的所有数据都是可以找到并进行解释的。很明显孤立的区域就是一种异常，因为解码器永远无法播放或检索到这个区域。通过识别嵌入TrueCrypt容器产生的空隙，我们还可以估计这个孤立区域的大小。


---


## 二、脚本（源代码）

提示：要注意python的版本是否兼容（下面代码）

### 2.1、tcsteg2.py：

```
#!/usr/bin/env python
"""
tcsteg2 -- TrueCrypt real steganography tool
version 2.0 (2012-02-18)
by Vladimir Ivanov &lt;vladimirivanov815@gmail.com&gt;
and Martin J. Fiedler &lt;martin.fiedler@gmx.net&gt;

see: http://keyj.emphy.de/real-steganography-with-truecrypt

This software is published under the terms of KeyJ's Research License,
version 0.2. Usage of this software is subject to the following conditions:
0. There's no warranty whatsoever. The author(s) of this software can not
   be held liable for any damages that occur when using this software.
1. This software may be used freely for both non-commercial and commercial
   purposes.
2. This software may be redistributed freely as long as no fees are charged
   for the distribution and this license information is included.
3. This software may be modified freely except for this license information,
   which must not be changed in any way.
4. If anything other than configuration, indentation or comments have been
   altered in the code, the original author(s) must receive a copy of the
   modified code.

Version history
===============

2.0 (Vladimir Ivanov, speed optimizations by Martin Fiedler)
- now supports files over 4 GiB
- erases duplicate encoder signature
- auto-renames TrueCrypt container
- supports 3gp videos
- function allowing post-embed password change

1.0 (Martin Fiedler)
- initial release
"""
import sys, os, struct

MAX_BUFFER_SIZE = 67108864   # 64 MiB
TC_HEADER_SIZE = 65536       # 64 KiB
MAX_INT32 = 4294967295
MAX_INT64 = 18446744073709551615L

class ProcessingError(RuntimeError):
    pass

################################################################################

class Atom(object):
    def __init__(self, f_src, name, start, header_size, size, mother):
        self.f_src = f_src
        self.name = name
        self.start = start
        self.size = size
        self.header_size = header_size
        self.mother = mother
        self.childs = []
        self.contents = None

    def setBodySize(self, bodySize):    
        oldBodySize = self.size - self.header_size
        bodyDiff = bodySize - oldBodySize
        hDiff = 0       
        if bodySize &lt;= MAX_INT32:
            if self.header_size != 8:
                self.header_size = 8
                hDiff = -8
        else:
            if self.header_size != 16:
                self.header_size = 16
                hDiff = 8
        self.size = self.header_size + bodySize
        if self.mother:
            oldParentBodySize = self.mother.size - self.mother.header_size
            self.mother.setBodySize(oldParentBodySize + hDiff + bodyDiff)
    def writeHeader(self, f_dest):
        if self.size &gt;= MAX_INT32 and self.header_size == 8:
            raise ProcessingError("Atom size too large for compact header")     
        # compact
        if self.size &lt;= MAX_INT32 and self.header_size == 8:
            f_dest.write(struct.pack("&gt;I4s", self.size, self.name))
        # extended
        else:
            f_dest.write(struct.pack("&gt;I4sQ", 1, self.name, self.size))
        return self.size - self.header_size

    def writePayload(self, f_dest):
        if self.childs:
            for atom in self.childs:
                atom.write(f_dest)
        else:
            dataBuffer = None
            bodySize = self.size - self.header_size
            if self.f_src:
                self.f_src.seek(self.start + self.header_size)
                percent_i = 0
                percent_f = 0.0
                if bodySize &gt; MAX_BUFFER_SIZE:
                    percent_incr = 100.0 * MAX_BUFFER_SIZE / bodySize
                else:
                    percent_incr = 0.0
                while bodySize &gt; 0:
                    if bodySize &gt; MAX_BUFFER_SIZE:
                        dataBuffer = self.f_src.read(MAX_BUFFER_SIZE)
                    else:
                        dataBuffer = self.f_src.read(bodySize)
                    f_dest.write(dataBuffer)
                    bodySize -= MAX_BUFFER_SIZE
                    percent_f += percent_incr
                    percent_i_new = min(100, int(percent_f))
                    if percent_i_new &gt; percent_i:
                        percent_i = percent_i_new
                        sys.stderr.write("%3d%% done\r" % percent_i)
                        sys.stderr.flush()
            elif self.contents:
                if bodySize == len(self.contents):
                    f_dest.write(self.contents)
                else:
                    raise ProcessingError("Atom content size does not equal body size")
            else:
                if bodySize &gt; 0:
                    f_dest.seek(bodySize - 1, 1)
                    byte = f_dest.read(1)
                    if not byte:
                        f_dest.write("\0")
                    else:
                        f_dest.seek(-1, 1)
                        f_dest.write(byte)

    def write(self, f_dest):
        self.writeHeader(f_dest)
        self.writePayload(f_dest)

################################################################################

def AnalyseFile(f):
    atoms = None
    try:
        atoms = parseAtoms(f, 0, os.fstat(f.fileno()).st_size, None)
    except Exception, e:
        raise ProcessingError("Parse Error: " + str(e))
    return atoms

def parseAtoms(f, start, end, mother):
    offset = start
    atomSize = None
    atomHeaderSize = None
    comrades = []
    try:
        while offset &lt; end:
            f.seek(offset)      
            atomSize = struct.unpack("&gt;I", f.read(4))[0]
            atomType = struct.unpack("&gt;4s", f.read(4))[0]
            if atomSize == 1:
                atomSize = struct.unpack("&gt;Q", f.read(8))[0]
                atomHeaderSize = 16 # Extended
            else:
                atomHeaderSize = 8  # Compact
                if atomSize == 0:
                    atomSize = end - offset
            if start + atomSize &gt; end:
                raise ProcessingError("Invalid size for atom '" + atomType + "' @ " + hex(offset))
            atom = Atom(f, atomType, offset, atomHeaderSize, atomSize, mother)
            if mother:
                mother.childs.append(atom)
            comrades.append(atom)
            if atomType in ["moov","trak","mdia","minf","stbl"]:
                atom.childs = parseAtoms(f, offset + atomHeaderSize, offset + atomSize, atom)
            offset = offset + atomSize
    except struct.error, e:
        raise ProcessingError("Atom header must be multiples 4 or 8 near " + hex(offset))
    except Exception, e:
        raise ProcessingError(str(e))
    return comrades

def findAtom(atoms, name):
    aList = []
    for a in atoms:
        if a.name == name:
            aList.append(a)
        aList = aList + findAtom(a.childs, name)
    return aList

def printAtoms(atoms, l=0):
    for a in atoms:
        print "%s %s %ld @ 0x%lx" % ("   "*l, a.name, a.size, a.start)
        printAtoms(a.childs,l+1)

def adjustSampleOffsets(atoms, offset):
    sampleAtoms = findAtom(atoms, "stco") + findAtom(atoms, "co64")
    if len(sampleAtoms) == 0:
        raise ProcessingError("Could not find any 'stco' or 'co64' atoms")
    for sAtom in sampleAtoms:
        sAtom.f_src.seek(sAtom.start + sAtom.header_size)
        verFlags, count = struct.unpack("&gt;II", sAtom.f_src.read(8))
        if sAtom.name == "stco":
            sampleOffsets = struct.unpack('&gt;' + 'I' * count, sAtom.f_src.read(count * 4))
        elif sAtom.name == "co64":
            sampleOffsets = struct.unpack('&gt;' + 'Q' * count, sAtom.f_src.read(count * 8))
        sampleOffsets = [x + offset for x in sampleOffsets]
        # Does the atom need to support 64-bit values?
        if max(sampleOffsets) &gt; MAX_INT32 and sAtom.name == "stco":
            sAtom.name = "co64"
        sAtom.contents = struct.pack("&gt;II", verFlags, count)
        if sAtom.name == "stco":
            sAtom.contents += struct.pack('&gt;' + 'I' * count, *sampleOffsets)
        elif sAtom.name == "co64":
            sAtom.contents += struct.pack('&gt;' + 'Q' * count, *sampleOffsets)
        if (sAtom.size - sAtom.header_size) != len(sAtom.contents):
            sAtom.setBodySize(len(sAtom.contents))      
        sAtom.f_src = None
    return min(sampleOffsets)

def TCSteg_Embed(atoms, tcFile):
    ftyp = findAtom(atoms, "ftyp")
    mdat = findAtom(atoms, "mdat")
    moov = findAtom(atoms, "moov")
    if len(ftyp) != 1 or len(mdat) != 1 or len(moov) != 1:
        printAtoms(atoms)
        raise ProcessingError("One of each type required to embed: ['ftyp','mdat','moov']\nWe do not support this.")
    ftyp = ftyp[0]
    mdat = mdat[0]
    moov = moov[0]
    tcFileSize = os.fstat(tcFile.fileno()).st_size
    tcPreservedSize = tcFileSize - (TC_HEADER_SIZE * 3)
    tcStartHeaderVolBackup = tcFileSize - (TC_HEADER_SIZE * 2)
    mdatRealBodySize = mdat.size - mdat.header_size
    mdatEndMarker = tcFileSize - (TC_HEADER_SIZE * 2) + (mdatRealBodySize)
    mdatNewSize = mdatEndMarker - ftyp.size
    tcFile.seek(0)
    if ftyp.size + 16 &gt; TC_HEADER_SIZE:
        raise ProcessingError("'ftyp' atom + 'mdat' headers too long")
    ftyp.write(tcFile)
    tempH = mdat.header_size
    tempL = mdat.size
    if mdatNewSize &lt;= MAX_INT32:
        Atom(None, "free", None, 8, 8, None).write(tcFile)
        mdatNewSize = mdatNewSize - 8
        mdat.size = mdatNewSize
        mdat.header_size = 8
        mdat.writeHeader(tcFile)
    else:
        mdat.size = mdatNewSize
        mdat.header_size = 16
        mdat.writeHeader(tcFile)
    mdat.header_size = tempH
    mdat.size = tempL

    # re-generate first 64 KiB
    voidRegionSize = TC_HEADER_SIZE - tcFile.tell()
    mdat.f_src.seek(mdat.start + mdat.header_size)
    tcFile.write(mdat.f_src.read(voidRegionSize)) 
    
    # start header volume backups. Last 128 KiB of tc_file
    tcFile.seek(tcStartHeaderVolBackup)

    # Mark the position of the real mdat sample start
    mdatOffset = tcFile.tell() - (mdat.start + mdat.header_size)
    mdat.writePayload(tcFile)
    if tcFile.tell() != mdatEndMarker:
        raise ProcessingError("Wrote more mdat than we should have")

    # fix mdat shift by offsetting to each sample chunk
    print "Fixing up hybrid file ..."
    firstSample = adjustSampleOffsets(atoms, mdatOffset)

    # Destory duplicate encoder signature before first sample.
    tcFile.seek(tcStartHeaderVolBackup)
    tcFile.write(os.urandom(min(firstSample - tcStartHeaderVolBackup, TC_HEADER_SIZE)))
    tcFile.seek(mdatEndMarker) 
    moov.write(tcFile)
    
def Pass_Helper(video_path):
    f = None
    try:
        f = open(video_path, "rb+")
        last = AnalyseFile(f)[-1]
        if last.name == "skip":
            print "Removing padding 'skip' atom"
            f.truncate(last.start)
            print "Removal completed successfully"
        else:
            print "Preparing hybrid file for password change ... "
            f.seek(0, 2)
            Atom(None, "skip", None, 8, 8 + TC_HEADER_SIZE * 2, None).write(f)
            print "Complete.  Now change the TrueCrypt password"
    except IndexError:
        pass
    except IOError:
        print &gt;&gt;sys.stderr, "Error opening file '"+video_path+"'"
    except Exception, e:
        print &gt;&gt;sys.stderr, str(e)
    if f:
        f.close()

################################################################################

if __name__ == "__main__":
    supported_formats = ["mov","qt","mp4","m4v","m4a","3gp"]
    if len(sys.argv) &lt; 3:
        pname = sys.argv[0].split(os.sep)[-1]
        print "too few arguments"
        print "Usage (1):", pname, "&lt;MP4 Video&gt; &lt;TrueCrypt Container&gt;"
        print "Embeds a file into a TrueCrypt container so that both are still readable."
        print
        print "&lt;MP4 Video&gt; is a file in one of the following formats:"
        print "   QuickTime / ISO MPEG-4  (%s)" % (", ".join(["*." + fmt for fmt in supported_formats]))
        print
        print "&lt;TrueCrypt Container&gt; is a TrueCrypt hidden volume. The file will be"
        print "modified in-place so that it seems like a copy of the input file that can be"
        print "opened in an appropriate viewer/player. However, the hidden TrueCtype volume"
        print "will also be preserved and can be used."
        print
        print
        print "Usage (2):", pname, "-p &lt;Hybrid File&gt;"
        print "&lt;Hybrid File&gt; is a file that is both TrueCrypt container and a video."
        print "This file will be modified in-place to make it possible to change the TrueCrypt"
        print "password. After changing the password, this command should be run again to"
        print "remove that (detectable and hence insecure) modification!"
        print
        print
        sys.exit(2)

    if sys.argv[1] == "-p":
        Pass_Helper(sys.argv[2])
        sys.exit(0) 
    video_path = sys.argv[1]
    tc_path = sys.argv[2]
    video_file = None
    tc_file = None
    tcSize = 0
    try:
        video_file = open(video_path, "rb")
    except IOError, e:
        print &gt;&gt;sys.stderr, "Error opening file '"+video_path+"'"
        sys.exit(1)
    try:
        tc_file = open(tc_path, "rb+")
        tcSize = os.path.getsize(tc_path)
    except IOError, e:
        print &gt;&gt;sys.stderr, "Error opening file '"+tc_path+"'"
        sys.exit(1)
    try:
        video_ext = os.path.splitext(video_path)[1].lstrip(".")
        if video_ext in supported_formats:  
            print "Parsing video ..."
            atoms = AnalyseFile(video_file)
            print "Embedding ... be patient"
            TCSteg_Embed(atoms, tc_file)
            tc_file.close()
            if not tc_path.endswith("." + video_ext):
                if not os.path.exists(tc_path + "." + video_ext):
                    new_tc_path = tc_path + "." + video_ext
                    os.rename(tc_path, new_tc_path)
                    tc_path = new_tc_path
            print "Hybrid file '%s' was created successfully." % tc_path
            print
            print "Everything OK. Try mounting the file in TrueCrypt and playing the video."
        else:
            print &gt;&gt;sys.stderr, "Error: input video format is not supported"
    except (ProcessingError, IOError), e:
        print &gt;&gt;sys.stderr, "ERROR:", e
        tc_file.truncate(tcSize)
    finally:
        video_file.close()
        tc_file.close()
```

### 2.2、jpegEOFx.py

```
import sys
import struct
import os

#JPEG Segment markers

SOI = 0xFFD8 # Start of Image - Fixed size
SOF0 = 0xFFC0 # Start of Frame (Baseline DCT)
SOF2 = 0xFFC2 # Start of Frame (Progressive DCT)
DHT = 0xFFC4 # Define Huffman Table(s)
DQT = 0xFFDB # Define Quantization Table(s)
DRI = 0xFFDD # Define Restart Interval
SOS = 0xFFDA # Start of Scan
RST0 = 0xFFD0 # Restart (0-7) - Fixed size
APP0 = 0xFFE0 # Application-specific (0-F)
COM = 0xFFFE # Comment
EOI = 0xFFD9 # End of Image - Fixed size

RST_MASK = 0xFFD8
APP_MASK = 0xFFF0
FIELD_LENGTH = 2

# Parse JPEG segments until the end of image marker is
# encountered. Returns the Payload as a string.

def extractPayload(fp):
	fp.seek(0)

	offset = 0
	length = None
	startofPayload = 0

	while True:
		offset = fp.tell()

		# Read segment marker
		marker = struct.unpack("&gt;H", fp.read(2))[0]

		# Handle variable size segments with trailing length field
		if marker in [SOF0,SOF2,DHT,DQT,DRI,COM] or (marker&amp;APP_MASK)==APP0:
			# Read length Big-endian int16
			length = struct.unpack("&gt;H",fp.read(2))[0]

			# Seek to next segment marker
			fp.seek(length - FIELD_LENGTH, 1)
		# Handle fixed size segments
		elif marker in [SOI,EOI] or (marker&amp;RST_MASK)==RST0:
			length = FIELD_LENGTH
		# entropy-coded data, any 0xFF byte will be followed by 0x00 unless it is a marker
		elif marker == SOS:
			# Read file remainder into buffer
			buff = fp.read()

			# Search until EOI marker is found
			eoi_pos = buff.find("\xFF\xD9")

			if eoi_pos &lt; 0 :
				print &gt;&gt;sys.stderr, "ERROR : Corrupt JPEG. Cannot find End of Image marker."

				return None
			else:
				return buff[ eoi_pos + FIELD_LENGTH:]
		else:
			print &gt;&gt;sys.stderr, "ERROR : Unknown marker 0x" + hex(marker&amp;0xFFFF)
			sys.exit(1)
		#endif
	# endwhile

	return None
#enddef

if __name__ == "__main__":
	if len(sys.argv) &lt; 3:
		print "Usage : jpegEOFx.py &lt;INPUT JPEG&gt; &lt;OUTPUT PAYLOAD&gt;"
		sys.exit(2)

	jpegFile = open(sys.argv[1], "rb")

	# Check if file is JPEG
	if jpegFile.read(2) != "\xFF\xD8":
		print &gt;&gt;sys.stderr, "ERROR : File is not a JPEG image."
		sys.exit(1)

	payload = extractPayload(jpegFile)

	# Write payload to output file
	if payload:
		print "Found an extra", len(payload), "bytes after End of Image marker."
		outFile = open(sys.argv[2], "wb")
		outFile.write(payload)
		outFile.close()

	jpegFile.close()
```

### 2.3、detect anomalies in video files.py

```
#!/usr/bin/env python

# http://www.forensicmag.com/product-releases/2012/01/python-script-detect-hidden-data
# January 2012 Discovering the Hidden Column by C. Hosmer
# DFI Column Python Script Sample Method to Detect TCSTEGO Data Hiding
# Version .90 
# Source is released for public use provided that you reference the source article

# IMPORTS

import struct # used for packing/unpacking binary data
import sys # command line arguments
import os.path # file handling

# constants
DEFAULTPOSITION = -1
MB_100 = 104857600
GB = 1073741824
MB = 1048576
KB = 1024
THRESHOLD = 48 #BYTES
START_POS = 12 # SKIPS OVER 4 byte container name stco, 4 byte version + flags, 4 byte number of elements (count)
STCO_STR = "stco\0\0\0\0"
STCO_LEN = 8
BIGINDIAN = "&gt;I"
STEG_SUSPECTED = "Stego Suspected detected Orphan Chunk : %s"
STEG_NOT_SUSPECTED = "NO Stego Suspected No Orphans Found"

"""
FUNCTION: ffind
This functions purpose to find the stco table in a file, without loading the whole file.
Loading the whole file may cause memory errors
"""
def ffind(fh, target, offset=0):
    buff = []
    pos = DEFAULTPOSITION
    fh.seek(offset)
    ft = DEFAULTPOSITION

    while True:
        buff = fh.read(MB_100) #100 MB read
        pos = buff.find(target)
        if pos != DEFAULTPOSITION:
            pos = fh.tell() - len(buff) + pos
            break
        #endif

        fh.seek(fh.tell() - len(target))
        
        # if we backtracked to the same place then EOF
        if ft &gt;= fh.tell():
            break
        else:
            ft = fh.tell()
        #endif
    #endwhile
    fh.seek(offset)
    return pos
    #enddef

"""
FUNCTION: formatBytes
This functions converts bytes into a more appropriate unit, if needed
"""
def formatBytes(bytes):
    bytes = float(bytes)
    if bytes &gt;= GB:
        gigabytes = bytes / GB
        string = '%.2f GB' % gigabytes
    elif bytes &gt;= MB:
        megabytes = bytes / MB
        string = '%.2f MB' % megabytes
    elif bytes &gt;= KB:
        kilobytes = bytes / KB
        string = '%.2f KB' % kilobytes
    else:
        string = '%.2f ' % bytes
    return string

if __name__ == '__main__':

    if len(sys.argv) &lt; 2:
       print "Please provide a file to analyze..."
       sys.exit() # check that they provided a file
    if os.path.exists(sys.argv[1]) == False:
       print "The file does not exists, please provide a valid path"
       sys.exit()

    #open QuickTime / ISO MPEG-4 ### mov,qt,mp4,m4v,m4a
    fileIn = open(sys.argv[1], 'rb')
    
    mdat_pos = ffind(fileIn,"mdat")
    
    print ""
    print "Scanning File ..."
    # print "MDAT @", mdat_pos

    stco_pos = 0
    foundMdatRef = False
    minimum = sys.maxint
    
    #seacrh for Sample Table Chunk Offsets
    
    while stco_pos &gt; DEFAULTPOSITION:

        stco_pos = ffind(fileIn,STCO_STR, stco_pos + STCO_LEN)

        #quit no STCO struct found
        if stco_pos == DEFAULTPOSITION:
            break
        
        # print "STCO @", stco_pos

        # Determine length and buffer the STCO table
        fileIn.seek(stco_pos - 4)
        sLen = struct.unpack(BIGINDIAN,fileIn.read(4))[0]
        sTable = fileIn.read(sLen)

        count = struct.unpack(BIGINDIAN,sTable[8:12])[0]
        # print "Records in STCO atom:", count

        # Mark the start and end of STCO structure
        startChunkOffsets = START_POS
        endChunkOffsets = startChunkOffsets + (count*4)
 
        # Iterate over the chunkOffsets
        diff = 0
        firstRecord = True

        while startChunkOffsets &lt;= endChunkOffsets - 4:
            offset = struct.unpack(BIGINDIAN,sTable[startChunkOffsets:startChunkOffsets+4])[0]
            diff = offset - mdat_pos + 4
            
            minimum = min(diff,minimum)
         
            #If any chunk references the begining of mdat, quit not-stegged
            if offset == (mdat_pos + 4):
                foundMdatRef = True
                break
            startChunkOffsets += 4
    
        #endwhile

    #endwhile

    print ""
    
    if foundMdatRef or minimum &lt;= THRESHOLD:
        print STEG_NOT_SUSPECTED
    else:
        print STEG_SUSPECTED % (formatBytes(minimum))
        print "Starting at MDAT Offset :", hex(offset)
        
    #close the QuickTime / ISO MPEG-4 ### mov,qt,mp4,m4v,m4a file
    fileIn.close()
```
