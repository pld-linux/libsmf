# NOTE: original maintenance (at sf.net) stopped in 2010
# some continuation from 2013 is available at https://github.com/stump/libsmf
Summary:	Standard MIDI File library
Summary(pl.UTF-8):	Biblioteka obsługi formatu Standard MIDI File
Name:		libsmf
Version:	1.3
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libsmf/%{name}-%{version}.tar.gz
# Source0-md5:	eb698f1bc0bad9d5bce4c10386347486
URL:		http://sourceforge.net/projects/libsmf/
BuildRequires:	glib2-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	glib2 >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standard MIDI File library.

%description -l pl.UTF-8
Biblioteka obsługi formatu Standard MIDI File.

%package devel
Summary:	Header files for SMF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SMF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2

%description devel
Header files for SMF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SMF.

%package static
Summary:	Static SMF library
Summary(pl.UTF-8):	Statyczna biblioteka SMF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SMF library.

%description static -l pl.UTF-8
Statyczna biblioteka SMF.

%prep
%setup -q

%build
%configure \
	--with-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmf.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS TODO
%attr(755,root,root) %{_bindir}/smfsh
%attr(755,root,root) %{_libdir}/libsmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmf.so.0
%{_mandir}/man1/smfsh.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmf.so
%{_includedir}/smf.h
%{_pkgconfigdir}/smf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmf.a
