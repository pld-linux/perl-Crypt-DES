%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-DES perl module
Summary(pl):	Modu³ perla Crypt-DES
Name:		perl-Crypt-DES
Version:	1.01
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz
Patch:		perl-Crypt-DES-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Crypt/DES/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Crypt/DES
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitearch}/Crypt/DES.pm

%dir %{perl_sitearch}/auto/Crypt/DES
%{perl_sitearch}/auto/Crypt/DES/.packlist
%{perl_sitearch}/auto/Crypt/DES/DES.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/DES/DES.so

%{_mandir}/man3/*
