Summary:	Allegro GUI toolkit
Summary(pl.UTF-8):	Zestaw narzędzi GUI używający Allegro
Name:		tgui
Version:	0.9
Release:	0.1
License:	MIT
Group:		Development/Tools
Source0:	http://trent.gamblin.ca/tgui/%{name}-%{version}.tar.bz2
# Source0-md5:	89d9653c1e732a2a4324cc986f8892e8
Patch0:		%{name}-Makefile.patch
URL:		http://trent.gamblin.ca/tgui/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TGUI is an extensible GUI toolkit that uses Allegro for input. It is
written in C++. The basic widget set is very plain, but the main
purpose of TGUI is to allow users to create their own widgets, to be
used in games and perhaps other applications.

%description -l pl.UTF-8
TGUI jest elastycznym zestawem narzędzi napisanym w C++ używającym
biblioteki Allegro. Podstawowy widget jest bardzo prosty, ale TGUI
umożliwia użytkownikom tworzenie ich własnych widgetów do gier lub
innych aplikacji.

%package devel
Summary:	TGUI header files
Summary(pl.UTF-8):	Pliki nagłówkowe TGUI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for TGUI.

%description devel -l pl.UTF-8
Pliki nagłówkowe TGUI.

%package static
Summary:	TGUI static libraries
Summary(pl.UTF-8):	Biblioteki statyczne TGUI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
TGUI static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne TGUI.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	FLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/TGUI

%files static
%defattr(644,root,root,755)
%{_libdir}/libtgui.a
