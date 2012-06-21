%define Werror_cflags %nil

%define libname %mklibname cw
%define libnamedevel %mklibname cw -d

Name:		unixcw
Version:	3.0.2
Release:	1	
Summary:	Shared library for Morse programs

Group:		Communications
License:	GPLv2+
URL:		http://sourceforge.net/projects/unixcw
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz

Patch0:		unixcw-3.0.2-config.patch
Patch1:		unixcw-3.0.2-destdir.patch
Patch2:		unixcw-3.0.2-parallel-make.patch
Patch3:		unixcw-3.0.2-qt4.patch

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
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

# Fix the encoding on the man pages to be UTF-8

%build
./configure --prefix=%{_prefix} \
	    --libdir=%{_libdir} \
	    --mandir=%{_mandir}
make 

%install
make install DESTDIR=%{buildroot}

# Get rid of static lib.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

#Fix permissions for binary files
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc AUTHORS COPYING README
%doc README
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libcw.so.3
%{_libdir}/libcw.so.3.0.1


%files -n %{libnamedevel}
%{_libdir}/libcw.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
