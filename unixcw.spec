%define major 4
%define libname %mklibname cw %{major}
%define libnamedevel %mklibname cw -d

Name:		unixcw
Version:	3.1.1
Release:	1	
Summary:	Shared library for Morse programs
Group:		Communications
License:	GPLv2+
URL:		https://sourceforge.net/projects/unixcw
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz

%description
The UnixCW utilities add a general purpose CW library to your system, and
a small set of applications based around this library.  These applications
form a Morse code tutor suite, useful for Amateur and Marine radio operators.


%package -n	%libname
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%libname
UnixCW libraries.


%package -n	%libnamedevel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%libnamedevel
UnixCW utility libraries.

%prep
%setup -q
%build
%configure2_5x --disable-static
%make 

%install
%makeinstall_std

#Fix permissions for binary files
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc AUTHORS COPYING README
%doc README
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libcw.so.%{major}*


%files -n %{libnamedevel}
%{_libdir}/libcw.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Aug 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.1.1-1
+ Revision: 814998
- version update 3.1.1
- imported package unixcw

