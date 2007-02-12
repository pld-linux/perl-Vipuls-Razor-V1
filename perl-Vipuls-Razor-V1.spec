#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Spam should not be propagated beyond necessity
Summary(pl.UTF-8):   Spam nie powinien być rozsiewany bez potrzeby
Name:		perl-Vipuls-Razor-V1
Version:	1.20
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/razor/razor-agents-%{version}.tar.gz
# Source0-md5:	3612455aca8221718d2bf4b94ca67197
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
%if %{with tests}
BuildRequires:	perl-Net-DNS
%endif
Obsoletes:	Razor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vipul's Razor is a distributed, collaborative, spam detection and
filtering network. Through user contribution, Razor establishes a
distributed and constantly updating catalogue of spam in propagation
that is consulted by email clients to filter out known spam. Detection
is done with statistical and randomized signatures that efficiently
spot mutating spam content. User input is validated through reputation
assignments based on consensus on report and revoke assertions which
in turn is used for computing confidence values associated with
individual signatures.

%description -l pl.UTF-8
Vipul's Razor to rozproszona, współpracująca sieć wykrywania spamu.
Przy udziale użytkowników Razor stanowi rozproszony i stale
uaktualniany katalog rozprzestrzenianego spamu, który jest odpytywany
przez klientów pocztowych w celu filtrowania znanego spamu. Wykrywanie
jest przeprowadzane za pomocą statystycznych i losowych sygnatur,
które efektywnie wykrywają mutującą się zawartość spamu. Wejście od
użytkowników jest kontrolowane poprzez przypisaną reputację bazowaną
na raportach i zapewnieniach, które służą do obliczania poziomów
ufności związanych z poszczególnymi sygnaturami.

%prep
%setup -q -n razor-agents-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man5

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install razor-whitelist.pod $RPM_BUILD_ROOT%{_mandir}/man5/razor-whitelist.5
install razor.conf $RPM_BUILD_ROOT%{_mandir}/man5/razor.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes sample.txt
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/Razor
%{perl_vendorlib}/Razor/*
%{_mandir}/man1/*
%{_mandir}/man5/*
