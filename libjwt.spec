Name:		libjwt
Version:	1.8.0
Release:	1%{?dist}
Summary:	JWT C library

Group:		Development/Libraries
License:	LGPL3
URL:		https://github.com/benmcollins/libjwt
Source0:	https://github.com/benmcollins/libjwt/archive/v1.8.0/libjwt-v1.8.0.tar.gz

BuildRequires:	autoconf jansson-devel openssl-devel
Requires:	jansson openssl-libs

%description
JWT C library.

%prep
%autosetup -n %{name}-%{version}
autoreconf -i


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
/usr/include/jwt.h
/usr/lib64/libjwt.a
/usr/lib64/libjwt.la
/usr/lib64/libjwt.so
/usr/lib64/libjwt.so.0
/usr/lib64/libjwt.so.0.3.1
/usr/lib64/pkgconfig/libjwt.pc
%doc



%changelog

