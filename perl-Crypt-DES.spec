%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DES
Summary:	Crypt::DES Perl module
Summary(cs):	Modul Crypt::DES pro Perl
Summary(da):	Perlmodul Crypt::DES
Summary(de):	Crypt::DES Perl Modul
Summary(es):	M�dulo de Perl Crypt::DES
Summary(fr):	Module Perl Crypt::DES
Summary(it):	Modulo di Perl Crypt::DES
Summary(ja):	Crypt::DES Perl �⥸�塼��
Summary(ko):	Crypt::DES �� ����
Summary(nb):	Perlmodul Crypt::DES
Summary(pl):	Modu� Perla Crypt::DES
Summary(pt):	M�dulo de Perl Crypt::DES
Summary(pt_BR):	M�dulo Perl Crypt::DES
Summary(ru):	������ ��� Perl Crypt::DES
Summary(sv):	Crypt::DES Perlmodul
Summary(uk):	������ ��� Perl Crypt::DES
Summary(zh_CN):	Crypt::DES Perl ģ��
Name:		perl-Crypt-DES
Version:	2.03
Release:	6
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b9a84e14214e74e71dd80f906a3db96
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DES - Perl interface to DES block cipher.

%description -l pl
Crypt::DES - modu� obs�uguj�cy algorytm szyfrowania DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
