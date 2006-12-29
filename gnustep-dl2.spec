Summary:	GNUstep Database Library 2
Summary(pl):	Druga wersja bibliotek baz danych GNUstepa
Name:		gnustep-dl2
Version:	0.10.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/%{name}-%{version}.tar.gz
# Source0-md5:	59ce3b8407cfdc6d25901e97e17c9cc5
URL:		http://www.gnustepweb.org/
BuildRequires:	Gorm-devel >= 1.1.0
BuildRequires:	gnustep-base-devel >= 1.11.0
BuildRequires:	gnustep-make-devel >= 1.11.0
BuildRequires:	postgresql-backend-devel >= 7.2
BuildRequires:	postgresql-devel >= 7.2
Requires:	gnustep-base >= 1.11.0
Obsoletes:	gnustep-db2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%description
The GNUstep Database Library 2 (GDL2) is a set of libraries to map
Objective-C objects to rows of relational database management systems
(RDBMS). It aims to be compatible with Enterprise Objects Framework
(EOF) as released with WebObjects 4.5 from Apple Inc.

%description -l pl
GNUstep Database Library 2 (GDL2), czyli druga wersja biblioteki baz
danych GNUstepa, to zbiór bibliotek odwzorowuj±cych obiekty
Objective-C na wiersze relacyjnych baz danych. Celem jest osi±gniêcie
zgodno¶ci z Enterprise Object Framework (EOF) wydanym wraz z
WebObjects 4.5 przez Apple Inc.

%package devel
Summary:	Header files for GNUstep Database Library
Summary(pl):	Pliki nag³ówkowe biblioteki baz danych GNUstepa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-base-devel >= 1.9.1
Obsoletes:	gnustep-db2-devel

%description devel
Header files for GNUstep Database Library.

%description devel -l pl
Pliki nag³ówkowe biblioteki baz danych GNUstepa.

%package postgresql
Summary:	PostgreSQL adaptor for GNUstep Database Library
Summary(pl):	Interfejs PostgreSQL dla biblioteki baz danych GNUstepa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gnustep-db2-postgresql

%description postgresql
PostgreSQL adaptor for GNUstep Database Library.

%description postgresql -l pl
Interfejs PostgreSQL dla biblioteki baz danych GNUstepa.

%package postgresql-devel
Summary:	Header files for GNUstep PostgreSQL adaptor
Summary(pl):	Pliki nag³ówkowe interfejsu PostgreSQL do GNUstepa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-postgresql = %{version}-%{release}
Requires:	postgresql-devel >= 7.2
Obsoletes:	gnustep-db2-postgresql-devel

%description postgresql-devel
Header files for GNUstep PostgreSQL adaptor.

%description postgresql-devel -l pl
Pliki nag³ówkowe interfejsu PostgreSQL do GNUstepa.

%prep
%setup -q

%build
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes
%configure

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes

# ugh, framework is recompiled
%{__make} install \
	OPTFLAG="%{rpmcflags}" \
	messages=yes \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	postgresql -p /sbin/ldconfig
%postun	postgresql -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_prefix}/System/Library/Libraries/libgnustep-db2*.so.*
%attr(755,root,root) %{_prefix}/System/Library/Libraries/libEOInterface.so.*
%attr(755,root,root) %{_prefix}/System/Tools/eoutil
%attr(755,root,root) %{_prefix}/System/Tools/gdlgsdoc

%dir %{_prefix}/System/Applications/DBModeler.app
%attr(755,root,root) %{_prefix}/System/Applications/DBModeler.app/DBModeler
%{_prefix}/System/Applications/DBModeler.app/Resources
%{_prefix}/System/Applications/DBModeler.app/library_paths.openapp

%dir %{_prefix}/System/Library/ApplicationSupport/Palettes
%dir %{_prefix}/System/Library/ApplicationSupport/Palettes/GDL2.palette
%attr(755,root,root) %{_prefix}/System/Library/ApplicationSupport/Palettes/GDL2.palette/GDL2
%{_prefix}/System/Library/ApplicationSupport/Palettes/GDL2.palette/Resources

%files devel
%defattr(644,root,root,755)

%{_prefix}/System/Library/Headers/EOAccess
%{_prefix}/System/Library/Headers/EOControl
%{_prefix}/System/Library/Headers/EOInterface
%{_prefix}/System/Library/Headers/EOModeler

%attr(755,root,root) %{_prefix}/System/Library/Libraries/libgnustep-db2*.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/libEOInterface.so

%{_prefix}/System/Library/Makefiles/Auxiliary/gdl2.make

%files postgresql
%defattr(644,root,root,755)
%dir %{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework
%{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Headers
%{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions
%{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/Current
%dir %{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/A
%{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/A/Resources
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/A/libPostgres95EOAdaptor.so.*

%attr(755,root,root) %{_prefix}/System/Library/Libraries/libPostgres95EOAdaptor.so.*

%files postgresql-devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/A/Headers
%{_prefix}/System/Library/Headers/Postgres95EOAdaptor
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Postgres95EOAdaptor.framework/Versions/A/libPostgres95EOAdaptor.so
%attr(755,root,root) %{_prefix}/System/Library/Libraries/libPostgres95EOAdaptor.so
