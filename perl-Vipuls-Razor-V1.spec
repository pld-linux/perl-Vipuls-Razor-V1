%include	/usr/lib/rpm/macros.perl
Summary:	Spam should not be propagated beyond necessity
Summary(pl):	Spam nie powinien byæ rozsiewany bez potrzeby
Name:		perl-Vipuls-Razor-V1
Version:	1.20
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://prdownloads.sourceforge.net/razor/razor-agents-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%description -l pl
Vipul's Razor to rozproszona, wspó³pracuj±ca sieæ wykrywania spamu.
Przy udziale u¿ytkowników Razor stanowi rozproszony i stale
uaktualniany katalog rozprzestrzenianego spamu, który jest odpytywany
przez klientów pocztowych w celu filtrowania znanego spamu. Wykrywanie
jest przeprowadzane za pomoc± statystycznych i losowych sygnatur,
które efektywnie wykrywaj± mutuj±c± siê zawarto¶æ spamu. Wej¶cie od
u¿ytkowników jest kontrolowane poprzez przypisan± reputacjê bazowan±
na raportach i zapewnieniach, które s³u¿± do obliczania poziomów
ufno¶ci zwi±zanych z poszczególnymi sygnaturami.

%prep
%setup -q -n razor-agents-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man5

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install razor-whitelist.pod $RPM_BUILD_ROOT%{_mandir}/man5/razor-whitelist.5
install razor.conf $RPM_BUILD_ROOT%{_mandir}/man5/razor.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes sample.txt
%attr(755, root, root) %{_bindir}/*
%dir %{perl_sitelib}/Razor
%{perl_sitelib}/Razor/*
%{_mandir}/man1/*
%{_mandir}/man5/*
