%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-DES perl module
Summary(pl):	Modu³ perla Crypt-DES
Name:		perl-Crypt-DES
Version:	1.01
Release:	4
License:	Distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-DES - Perl interface to DES block cipher.

%description -l pl
Crypt-DES - modu³ wspomagaj±cy algorytm DES.

%prep
%setup -q -n Crypt-DES-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Crypt/DES.pm
%dir %{perl_sitearch}/auto/Crypt/DES
%{perl_sitearch}/auto/Crypt/DES/DES.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/DES/DES.so
%{_mandir}/man3/*
