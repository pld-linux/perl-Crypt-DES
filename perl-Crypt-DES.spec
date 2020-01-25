#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	DES
Summary:	Crypt::DES - Perl DES encryption module
Summary(pl.UTF-8):	Crypt::DES - moduł Perla dla szyfrowania DES
Name:		perl-Crypt-DES
Version:	2.07
Release:	10
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e845d24cf383ca4a30a3380a2735feac
URL:		http://search.cpan.org/dist/Crypt-DES/
%{?with_tests:BuildRequires:	perl-Crypt-CBC}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DES is Perl interface to DES block cipher.

%description -l pl.UTF-8
Moduł Perla Crypt::DES zawiera obsługę algorytmu szyfrowania DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/DES/DES.so
%{_mandir}/man3/Crypt::DES.3pm*
