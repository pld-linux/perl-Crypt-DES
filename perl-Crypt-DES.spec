%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DES
Summary:	Crypt::DES Perl module
Summary(cs):	Modul Crypt::DES pro Perl
Summary(da):	Perlmodul Crypt::DES
Summary(de):	Crypt::DES Perl Modul
Summary(es):	Módulo de Perl Crypt::DES
Summary(fr):	Module Perl Crypt::DES
Summary(it):	Modulo di Perl Crypt::DES
Summary(ja):	Crypt::DES Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::DES ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::DES
Summary(pl):	Modu³ Perla Crypt::DES
Summary(pt):	Módulo de Perl Crypt::DES
Summary(pt_BR):	Módulo Perl Crypt::DES
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::DES
Summary(sv):	Crypt::DES Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::DES
Summary(zh_CN):	Crypt::DES Perl Ä£¿é
Name:		perl-Crypt-DES
Version:	2.03
Release:	4
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DES - Perl interface to DES block cipher.

%description -l pl
Crypt::DES - modu³ obs³uguj±cy algorytm szyfrowania DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%{perl_sitearch}/Crypt/DES.pm
%dir %{perl_sitearch}/auto/Crypt/DES
%{perl_sitearch}/auto/Crypt/DES/DES.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/DES/DES.so
%{_mandir}/man3/*
