# TODO
# - at this time package do not build with dbus support
#   I do not need it ...
# Conditional build:
%bcond_with	dbus	# build with dbus support

#
Summary:	Service daemon for mediating access to a GPS
Summary(pl):	Oprogramowanie komunikuj±ce siê z GPS'em
Name:		gpsd
Version:	2.30
Release:	1.1
License:	BSD
Group:		Daemons
Source0:	http://download.berlios.de/gpsd/%{name}-%{version}.tar.gz
# Source0-md5:	dde177174878e8ae6db15f8010da46dd
Patch0:		%{name}-ncurses.patch
URL:		http://gpsd.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	openmotif-devel
BuildRequires:	XFree86-devel
%if %{with dbus}
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libx11dir	%{_prefix}/lib/X11
%define		_appdefsdir	%{_libx11dir}/app-defaults

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

%package -n gpsd-devel
Summary:	Client libraries in C and Python for talking to a running gpsd or GPS
Group:		Development/Libraries
Requires:	gpsd

%description -n gpsd-devel
This package provides C header files for the gpsd shared libraries
that manage access to a GPS for applications; also Python modules. You
will need to have gpsd installed for it to work.

%package -n gpsd-clients
Summary:	Clients for gpsd with an X interface
Group:		Applications/System
Requires:	openmotif-libs
Requires:	gpsd

%description -n gpsd-clients
xgps is a simple test client for gpsd with an X interface. It displays
current GPS position/time/velocity information and (for GPSes that
support the feature) the locations of accessible satellites.

xgpsspeed is a speedometer that uses position information from the
GPS. It accepts an -h option and optional argument as for gps, or a -v
option to dump the package version and exit. Additionally, it accepts
- -rv (reverse video) and -nc (needle color) options.

cgps resembles xgps, but without the pictorial satellite display. It
can run on a serial terminal or terminal emulator.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_dbus: --enable-dbus}

%{__make}
%{__python} -c "import compiler;compiler.compileFile('gps.py')"
%{__python} -c "import compiler;compiler.compileFile('gpsfake.py')"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/hotplug/usb,%{py_sitedir},%{_appdefsdir},%{_datadir}/gpsd/}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gps.pyc gpsfake.pyc $RPM_BUILD_ROOT/%{py_sitedir}/
install gpsd.hotplug gpsd.usermap $RPM_BUILD_ROOT/%{_sysconfdir}/hotplug/usb/
install xgps.ad $RPM_BUILD_ROOT/%{_appdefsdir}/xgps
install xgpsspeed.ad $RPM_BUILD_ROOT/%{_appdefsdir}/xgpsspeed
install dgpsip-servers $RPM_BUILD_ROOT/%{_datadir}/gpsd/dgpsip-servers

%clean
rm -rf $RPM_BUILD_ROOT

#%post -n gpsd
#/sbin/ldconfig

#%postun -n gpsd
#/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL COPYING TODO AUTHORS HACKING
%attr(755,root,root) %{_sbindir}/gpsd
%attr(755,root,root) %{_bindir}/gpsprof
%attr(755,root,root) %{_bindir}/sirfmon
#%{_libdir}/libgps.la
#%attr(755,root,root) %{_libdir}/libgps.so*
#%{_libdir}/libgps.a
%attr(755,root,root) %{_libdir}/libgps.so.15*
%{_mandir}/man8/gpsd.8*
%{_mandir}/man1/gpsprof.1*
%{_mandir}/man1/sirfmon.1*
%{_sysconfdir}/hotplug/usb/gpsd.hotplug
%{_sysconfdir}/hotplug/usb/gpsd.usermap
%{_datadir}/gpsd/dgpsip-servers
%{py_sitedir}/gps.pyc

%files -n gpsd-clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgps
%attr(755,root,root) %{_bindir}/xgpsspeed
%attr(755,root,root) %{_bindir}/cgps
%attr(755,root,root) %{_bindir}/gpspipe
%{?with_dbus: %attr(755,root,root) %{_bindir}/gpxlogger}
%{_mandir}/man1/xgps.1*
%{_mandir}/man1/gpspipe.1*
%{?with_dbus: %{_mandir}/man1/gpxlogger.1*}
%{_appdefsdir}/xgps
%{_appdefsdir}/xgpsspeed

%files -n gpsd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpsfake
%attr(755,root,root) %{_bindir}/rtcmdecode
%attr(755,root,root) %{_bindir}/gpsflash
%{py_sitedir}/gpsfake.pyc
%{_includedir}/gps.h
%{_includedir}/libgpsmm.h
%{_includedir}/gpsd.h
%{_mandir}/man1/gpsfake.1*
%{_mandir}/man1/rtcmdecode.1*
%{_mandir}/man1/gpsflash.1*
%{_mandir}/man3/libgps.3*
%{_mandir}/man3/libgpsmm.3*
%{_mandir}/man3/libgpsd.3*
%{_mandir}/man5/rtcm-104.5*
%{_mandir}/man5/srec.5*
