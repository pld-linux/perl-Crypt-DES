#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DES
Summary:	Crypt::DES - Perl DES encryption module
Summary(pl):	Crypt::DES - modu³ Perla dla szyfrowania DES
Name:		perl-Crypt-DES
Version:	2.03
Release:	6
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b9a84e14214e74e71dd80f906a3db96
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DES is Perl interface to DES block cipher.

%description -l pl
Modu³ Perla Crypt::DES zawiera obs³ugê algorytmu szyfrowania DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%{perl_vendorarch}/Crypt/DES.pm
%dir %{perl_vendorarch}/auto/Crypt/DES
%{perl_vendorarch}/auto/Crypt/DES/DES.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/DES/DES.so
%{_mandir}/man3/*
