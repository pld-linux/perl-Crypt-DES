%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-DES perl module
Summary(pl):	Modu³ perla Crypt-DES
Name:		perl-Crypt-DES
Version:	2.03
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-DES - Perl interface to DES block cipher.

%description -l pl
Crypt-DES - modu³ wspomagaj±cy algorytm DES.

%prep
%setup -q -n Crypt-DES-%{version}

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
%{perl_sitearch}/Crypt/DES.pm
%dir %{perl_sitearch}/auto/Crypt/DES
%{perl_sitearch}/auto/Crypt/DES/DES.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/DES/DES.so
%{_mandir}/man3/*
