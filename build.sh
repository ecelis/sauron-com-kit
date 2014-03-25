cd third_party/ffmpeg-1.2.6
make distclean
./configure --enable-shared --disable-static --enable-memalign-hack
make
make install
cd ../pjproject-2.1.0
make distclean
rm -f pjmedia/include/pjmedia/config_auto.h
rm -f pjmedia/include/pjmedia-codec/config_auto.h
rm -f pjmedia/build/os-auto.mak
rm -f pjlib/include/pj/config_site.h 
rm -f pjlib/include/pj/compat/os_auto.h
rm -f pjlib/include/pj/compat/m_auto.h
rm -f pjlib/build/os-auto.mak
rm -f pjlib-util/build/os-auto.mak
rm -f build/os-auto.mak
rm -f build/cc-auto.mak
rm -f build.mak
./configure 
#--disable-video --disable-ffmpeg --disable-v4l2
CFLAGS="-fPIC" CXXFLAGS="-fPIC" make dep
CFLAGS="-fPIC" CXXFLAGS="-fPIC" make
## TODO python client not ready yet
cd pjsip-apps/src/python
python setup.py install

