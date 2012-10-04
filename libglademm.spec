Summary:	C++ wrappers for libglade
Name:		libglademm
Version:	2.6.7
Release:	14
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libglademm/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	f9ca5b67f6c551ea98790ab5f21c19d0
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libglade.

%package devel
Summary:	Devel files for libglademm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Devel files for libglademm.

%package apidocs
Summary:	Documentation for libglademm
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Documentation for libglademm.

%prep
%setup -q

sed -i -e "/GLIBMM_CHECK_PERL/d" configure.in

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install		\
	DESTDIR=$RPM_BUILD_ROOT	\
	docdir=%{_gtkdocdir}/%{name}-2.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %ghost %{_libdir}/libglademm*.so.?
%attr(755,root,root) %{_libdir}/libglademm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglademm*.so
%{_libdir}/libglademm*.la
%{_includedir}/%{name}-2.4
%{_libdir}/%{name}-2.4
%{_pkgconfigdir}/%{name}-2.4.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-2.4

