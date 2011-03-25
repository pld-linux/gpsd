#
# Conditional build:
%bcond_without	dbus	# build without dbus support
%bcond_without	bluez	# build without Bluetooth support
%bcond_without	x	# build without X Window System support
#
Summary:	Service daemon for mediating access to a GPS
Summary(pl.UTF-8):	Oprogramowanie komunikujące się z GPS-em
Name:		gpsd
Version:	2.96
Release:	1
License:	BSD
Group:		Daemons
Source0:	http://download.berlios.de/gpsd/%{name}-%{version}.tar.gz
# Source0-md5:	26a7a04d4298bc3a3a5d89fef4582b64
Patch0:		%{name}-link.patch
URL:		http://gpsd.berlios.de/
BuildRequires:	QtNetwork-devel >= 4.4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%if %{with dbus}
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
%endif
%{?with_bluez:BuildRequires:	bluez-libs-devel}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	libxslt-progs
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	qt4-qmake >= 4.4
BuildRequires:	rpm-pythonprov
BuildRequires:	xmlto
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		udevdir		/lib/udev

%description
gpsd is a service daemon that mediates access to a GPS sensor
connected to the host computer by serial or USB interface, making its
data on the location/course/velocity of the sensor available to be
queried on TCP port 2947 of the host computer. With gpsd, multiple GPS
client applications (such as navigational and wardriving software) can
share access to a GPS without contention or loss of data. Also, gpsd
responds to queries with a format that is substantially easier to
parse than NMEA 0183. A client library is provided for applications.

After installing this RPM, gpsd will automatically connect to USB
GPSes when they are plugged in and requires no configuration. For
serial GPSes, you will need to start gpsd by hand. Once connected, the
daemon automatically discovers the correct baudrate, stop bits, and
protocol. The daemon will be quiescent when there are no clients
asking for location information, and copes gracefully when the GPS is
unplugged and replugged.

%description -l pl.UTF-8
gpsd to demon usługi pośredniczącej w dostępie do sensora GPS
połączonego z komputerem poprzez interfejs szeregowy lub USB,
udostępniający dane o położeniu, kierunku ruchu i prędkości z sensora
na porcie TCP 2947 komputera. Przy użyciu gpsd wiele aplikacji
klienckich GPS (takich jak oprogramowanie nawigacyjne) może
współdzielić dostęp do GPS-a bez utraty danych. Ponadto gpsd odpowiada
na zapytania w formacie znacznie łatwiejszym do przetworzenia niż NMEA
0183. Dostarczona jest biblioteka kliencka dla aplikacji.

Po zainstalowaniu tego pakietu gpsd będzie się automatycznie łączył z
GPS-ami USB po podłączeniu ich. Dla GPS-ów szeregowych trzeba
uruchomić gpsd ręcznie. Po poączeniu demon automatycznie wykrywa
właściwą prędkość, liczbę bitów stopu i protokół. Demon oczekuje
spokojnie kiedy nie ma klientów i radzi sobie dobrze z odłączaniem i
ponownym podłączaniem GPS-a.

%package -n udev-gpsd
Summary:	UDEV support for GPS hotplugging
Summary(pl.UTF-8):	Obsługa UDEV-a do podłączania urządzeń GPS
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	udev-core >= 1:127

%description -n udev-gpsd
UDEV support for GPS hotplugging.

%description -n udev-gpsd -l pl.UTF-8
Obsługa UDEV-a do podłączania urządzeń GPS.

%package libs
Summary:	GPSd client library
Summary(pl.UTF-8):	Biblioteka kliencka GPSd
Group:		Libraries

%description libs
GPSd client library.

%description libs -l pl.UTF-8
Biblioteka kliencka GPSd.

%package devel
Summary:	Client libraries in C and Python for talking to a running gpsd or GPS
Summary(pl.UTF-8):	Biblioteki klienckie dla C i Pythona do komunikacji z gpsd lub GPS-em
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package provides C header files for the gpsd shared libraries
that manage access to a GPS for applications; also Python modules. You
will need to have gpsd installed for it to work.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe C dla bibliotek współdzielonych
gpsd zarządzających dostępem do GPS-a dla aplikacji, a także moduły
Pythona. Do działania bibliotek potrzebny jest gpsd.

%package static
Summary:	Static GPS client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka GPS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GPS client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka GPS.

%package qt-libs
Summary:	GPS Qt4 integration library
Summary(pl.UTF-8):	Biblioteka integrująca GPS z Qt4
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	QtNetwork >= 4.4

%description qt-libs
GPS Qt4 integration library.

%description qt-libs -l pl.UTF-8
Biblioteka integrująca GPS z Qt4.

%package qt-devel
Summary:	Development files for GPS Qt4 integration library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki integrującej GPS z Qt4
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt-libs = %{version}-%{release}
Requires:	QtNetwork-devel >= 4.4

%description qt-devel
Development files for GPS Qt4 integration library.

%description qt-devel -l pl.UTF-8
Pliki programistyczne biblioteki integrującej GPS z Qt4.

%package -n python-gps
Summary:	Python GPSd client library
Summary(pl.UTF-8):	Biblioteka kliencka GPSd dla Pythona
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-gps
GPSd client library for Python.

%description -n python-gps -l pl.UTF-8
Biblioteka kliencka GPSd dla Pythona.

%package clients
Summary:	Clients for gpsd
Summary(pl.UTF-8):	Aplikacje klienckie dla gpsd
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}

%description clients
cgps is a simple test client for gpsd. It displays current GPS
position/time/velocity information and (for GPSes that support the
feature) the locations of accessible satellites. cgps resembles xgps,
but without the pictorial satellite display. It can run on a serial
terminal or terminal emulator.

%description clients -l pl.UTF-8
cgps to prosty klient testowy dla gpsd. Wyświetla bieżące informacje
GPS o położeniu, czasie i prędkości oraz (w przypadku GPS-ów
obsługujących to) położenia dostępnych satelitów. Jest podobny do
xgps, ale nie ma rysunkowego przedstawiania satelitów. Może działać na
terminalu szeregowym lub emulatorze terminala.

%package clients-gui
Summary:	Clients for gpsd with an X interface
Summary(pl.UTF-8):	Aplikacje klienckie z interfejsem X
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-gps = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.0

%description clients-gui
xgps is a simple test client for gpsd with an X interface. It displays
current GPS position/time/velocity information and (for GPSes that
support the feature) the locations of accessible satellites.

xgpsspeed is a speedometer that uses position information from the
GPS.

%description clients-gui -l pl.UTF-8
xgps to prosty klient testowy dla gpsd z interfejsem X. Wyświetla
bieżące informacje GPS o położeniu, czasie i prędkości oraz (w
przypadku GPS-ów obsługujących to) położenia dostępnych satelitów.

xgpsspeed to prędkościomierz używający informacji o położeniu z GPS-a.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/include/ncurses" \
	%{?with_bluez:--enable-bluetooth} \
	%{?with_dbus:--enable-dbus} \
	%{!?with_x:--without-x}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT{%{udevdir},/etc/{udev/rules.d,sysconfig}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install gpsd.hotplug gpsd.hotplug.wrapper $RPM_BUILD_ROOT%{udevdir}
#install	gpsd.udev $RPM_BUILD_ROOT/etc/udev/rules.d/25-gpsd.rules
#install	gpsd.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/gpsd
install dgpsip-servers $RPM_BUILD_ROOT%{_datadir}/gpsd/dgpsip-servers

# check if missing header installation is up to date
[ ! -f $RPM_BUILD_ROOT%{_includedir}/libQgpsmm_global.h ] || exit 1
install libQgpsmm/libQgpsmm_global.h $RPM_BUILD_ROOT%{_includedir}

[ ! -d $RPM_BUILD_ROOT%{_desktopdir} ] || exit 1
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install packaging/X11/{xgps,xgpsspeed}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install packaging/X11/gpsd-logo.png $RPM_BUILD_ROOT%{_pixmapsdir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	qt-libs -p /sbin/ldconfig
%postun	qt-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL COPYING TODO AUTHORS
%attr(755,root,root) %{_sbindir}/gpsd
%attr(755,root,root) %{_bindir}/gpsmon
%{_mandir}/man8/gpsd.8*
%{_mandir}/man1/gpsmon.1*
%dir %{_datadir}/gpsd
%{_datadir}/gpsd/dgpsip-servers

%files -n udev-gpsd
%defattr(644,root,root,755)
%attr(755,root,root) %{udevdir}/gpsd.hotplug
%attr(755,root,root) %{udevdir}/gpsd.hotplug.wrapper
#/etc/udev/rules.d/25-gpsd.rules
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/gpsd

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpsd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpsd.so.0
%attr(755,root,root) %{_libdir}/libgps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgps.so.20

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpsdecode
%attr(755,root,root) %{_libdir}/libgps.so
%attr(755,root,root) %{_libdir}/libgpsd.so
%{_libdir}/libgps.la
%{_libdir}/libgpsd.la
%{_includedir}/gps.h
%{_includedir}/gpsd.h
%{_includedir}/libgpsmm.h
%{_pkgconfigdir}/libgps.pc
%{_pkgconfigdir}/libgpsd.pc
%{_mandir}/man1/gpsdecode.1*
%{_mandir}/man3/libgps.3*
%{_mandir}/man3/libgpsd.3*
%{_mandir}/man3/libgpsmm.3*
%{_mandir}/man5/srec.5*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgps.a
%{_libdir}/libgpsd.a

%files qt-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQgpsmm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQgpsmm.so.20

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQgpsmm.so
%{_libdir}/libQgpsmm.prl
%{_includedir}/libQgpsmm_global.h
%{_pkgconfigdir}/Qgpsmm.pc

%files -n python-gps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpscat
%attr(755,root,root) %{_bindir}/gpsfake
%attr(755,root,root) %{_bindir}/gpsprof
%dir %{py_sitedir}/gps
%attr(755,root,root) %{py_sitedir}/gps/*.so
%{py_sitedir}/gps/*.py[co]
%{py_sitedir}/gps-%{version}-py*.egg-info
%{py_sitedir}/gpscap.py[co]
%{_mandir}/man1/gpscat.1*
%{_mandir}/man1/gpsfake.1*
%{_mandir}/man1/gpsprof.1*

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpsctl
%attr(755,root,root) %{_bindir}/cgps
%attr(755,root,root) %{_bindir}/gpspipe
%{?with_dbus:%attr(755,root,root) %{_bindir}/gpxlogger}
%{_mandir}/man1/gpsctl.1*
%{_mandir}/man1/cgps.1*
%{_mandir}/man1/gps.1*
%{_mandir}/man1/gpspipe.1*

%if %{with x}
%files clients-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lcdgps
%attr(755,root,root) %{_bindir}/xgps
%attr(755,root,root) %{_bindir}/xgpsspeed
%{_mandir}/man1/lcdgps.1*
%{_mandir}/man1/xgps.1*
%{_mandir}/man1/xgpsspeed.1*
%{_desktopdir}/xgps.desktop
%{_desktopdir}/xgpsspeed.desktop
%{_pixmapsdir}/gpsd-logo.png
%endif
