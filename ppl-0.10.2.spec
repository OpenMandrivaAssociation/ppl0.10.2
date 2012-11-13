%define 	name			ppl0.10.2
%define 	version			0.10.2

%define		ppl_major		7
%define		libppl			%mklibname ppl %ppl_major

%define		ppl_c_major		2
%define		libppl_c		%mklibname ppl_c %ppl_c_major

%define		pwl_major		4
%define		libpwl			%mklibname pwl %pwl_major

Name:           %{name}
Version:        %{version}
Release:        %mkrel 3
Group:		Development/C
Summary:        The Parma Polyhedra Library: a library of numerical abstractions
License:        GPLv3+
URL:            http://www.cs.unipr.it/ppl/
Source0:        ftp://ftp.cs.unipr.it/pub/ppl/releases/0.12/ppl-0.10.2.tar.bz2
Source1:        ppl.hh
Source2:        ppl_c.h
Source3:        pwl.hh
Patch0:         ppl-0.10.2-Makefile.patch
Patch1:		ppl-0.10.2-gmp-5.0.patch
BuildRequires:  gmp-devel >= 4.1.3, gmpxx-devel >= 4.1.3, m4 >= 1.4.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

#-----------------------------------------------------------------------
%package	-n %{libppl}
Group:          Development/C
Summary:        The Parma Polyhedra Library: a library of numerical abstractions

%description	-n %{libppl}
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%files		-n %{libppl}
%defattr(-,root,root,-)
%{_libdir}/libppl.so.%{ppl_major}
%{_libdir}/libppl.so.%{ppl_major}.*

#-----------------------------------------------------------------------
%package	-n %{libppl_c}
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions

%description	-n %{libppl_c}
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%files		-n %{libppl_c}
%defattr(-,root,root,-)
%{_libdir}/libppl_c.so.%{ppl_c_major}
%{_libdir}/libppl_c.so.%{ppl_c_major}.*

#-----------------------------------------------------------------------
%package	-n %{libpwl}
Summary:        The Parma Watchdog Library: a C++ library for watchdog timers
Group:          Development/C++

%description	 -n %{libpwl}
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2).  This
package provides all what is necessary to run applications using the
PWL.  The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.

%files		-n %{libpwl}
%defattr(-,root,root,-)
%{_libdir}/libpwl.so.%{pwl_major}
%{_libdir}/libpwl.so.%{pwl_major}.*

#-----------------------------------------------------------------------
%prep
%setup -q -n ppl-0.10.2
%patch0 -p1
%patch1 -p0

%build
autoreconf -fi
%ifnarch ia64 ppc64 s390 s390x
%endif
%configure2_5x						\
	--docdir=%{_docdir}/%{name}-%{version}		\
	--disable-ppl_lcdd				\
	--disable-ppl_lpsol				\
	--enable-shared					\
	--disable-static				\
	--enable-interfaces="c++ c"
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std

# provide only binary compatibility package
rm -f %{buildroot}%{_bindir}/ppl-config
rm -fr %{buildroot}%{_includedir}
rm -fr %{buildroot}%{_libdir}/*.la
rm -fr %{buildroot}%{_libdir}/*.so
rm -fr %{buildroot}%{_datadir}/aclocal
rm -fr %{buildroot}%{_docdir}
rm -fr %{buildroot}%{_mandir}

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%if %mdkversion < 200900
%post -n %{libppl} -p /sbin/ldconfig

%post -n %{libppl_c} -p /sbin/ldconfig
%endif

#-----------------------------------------------------------------------
%if %mdkversion < 200900
%postun -n %{libppl} -p /sbin/ldconfig

%postun -n %{libppl_c} -p /sbin/ldconfig
%endif
