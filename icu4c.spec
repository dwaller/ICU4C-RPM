Name:           icu4c
Version:        4.8.1.1
Release:        1%{?dist}
Summary:        ICU - International Components for Unicode
Group:          Development/Tools
Packager:       Metaswitch Networks
License:        (C) IBM
URL:            http://site.icu-project.org

%description
Tools and utilities for developing with ICU.  ICU is a mature, widely used set of C/C++ and Java libraries providing Unicode and Globalization support for software applications. ICU is widely portable and gives applications the same results on all platforms and between C/C++ and Java software.
%prep
%build
%install
mkdir -p ${RPM_BUILD_ROOT}
tar xf ${RPM_SOURCE_DIR}/icu4c-4_8_1_1-RHEL6-x64.tgz -C ${RPM_BUILD_ROOT}
%pre
%post
%preun
%postun
%clean
rm -rf ${RPM_BUILD_ROOT}
%files
/usr/local/bin/gencfu
/usr/local/bin/uconv
/usr/local/bin/genbrk
/usr/local/bin/genrb
/usr/local/bin/gencnval
/usr/local/bin/genctd
/usr/local/bin/icuinfo
/usr/local/bin/makeconv
/usr/local/bin/derb
/usr/local/bin/icu-config
/usr/local/bin/pkgdata
/usr/local/sbin/genccode
/usr/local/sbin/gencmn
/usr/local/sbin/icupkg
/usr/local/sbin/gensprep
/usr/local/sbin/gennorm2
/usr/local/lib/libicutu.so
/usr/local/lib/libicuuc.so
/usr/local/lib/libicutu.so.48.1.1
/usr/local/lib/libicuuc.so.48
/usr/local/lib/libicule.so.48.1.1
/usr/local/lib/libicutest.so.48
/usr/local/lib/icu/
/usr/local/lib/libiculx.so.48
/usr/local/lib/libicutest.so.48.1.1
/usr/local/lib/pkgconfig/icu-le.pc
/usr/local/lib/pkgconfig/icu-i18n.pc
/usr/local/lib/pkgconfig/icu-lx.pc
/usr/local/lib/pkgconfig/icu-io.pc
/usr/local/lib/pkgconfig/icu-uc.pc
/usr/local/lib/libiculx.so
/usr/local/lib/libicuio.so
/usr/local/lib/libicutest.so
/usr/local/lib/libicui18n.so.48.1.1
/usr/local/lib/libicui18n.so.48
/usr/local/lib/libicule.so.48
/usr/local/lib/libicuuc.so.48.1.1
/usr/local/lib/libicuio.so.48.1.1
/usr/local/lib/libicudata.so.48.1.1
/usr/local/lib/libicuio.so.48
/usr/local/lib/libicui18n.so
/usr/local/lib/libicudata.so.48
/usr/local/lib/libicutu.so.48
/usr/local/lib/libicudata.so
/usr/local/lib/libicule.so
/usr/local/lib/libiculx.so.48.1.1
/usr/local/include/layout/
/usr/local/include/unicode/
/usr/local/share/icu/
/usr/local/share/man/man1/makeconv.1
/usr/local/share/man/man1/gencnval.1
/usr/local/share/man/man1/pkgdata.1
/usr/local/share/man/man1/derb.1
/usr/local/share/man/man1/uconv.1
/usr/local/share/man/man1/genctd.1
/usr/local/share/man/man1/genbrk.1
/usr/local/share/man/man1/genrb.1
/usr/local/share/man/man1/icu-config.1
/usr/local/share/man/man8/icupkg.8
/usr/local/share/man/man8/gencmn.8
/usr/local/share/man/man8/gensprep.8
/usr/local/share/man/man8/genccode.8

%changelog
