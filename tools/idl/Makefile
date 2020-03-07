
CC:=omniidl
CFLAGS:=-bpython
INCLUDELIBS:=-I/usr/include/openrtm-1.1/rtm/idl
pcIDL:=pcProcessPort
imIDL:=imProcessPort
infoIDL:=sv_GetInfo

all: $(pcIDL) $(imIDL) $(infoIDL)

pc: $(pcIDL).idl
	$(CC) $(INCLUDELIBS) $(CFLAGS) $(pcIDL).idl
	
im: $(imIDL).idl
	$(CC) $(INCLUDELIBS) $(CFLAGS) $(imIDL).idl
	
info: $(infoIDL).idl
	$(CC) $(INCLUDELIBS) $(CFLAGS) $(infoIDL).idl

%: %.idl
	$(CC) $(INCLUDELIBS) $(CFLAGS) $^

clean:
	rm -f *_idl.py *_idl.pyc 
	rm -rf _GlobalIDL*
	
