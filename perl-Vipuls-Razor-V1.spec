%include	/usr/lib/rpm/macros.perl
Summary:	Spam should not be propagated beyond necessity
Name:		perl-Vipuls-Razor-V1
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://prdownloads.sourceforge.net/razor/razor-agents-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vipul's Razor is a distributed, collaborative, spam detection and filtering
network. Through user contribution, Razor establishes a distributed and
constantly updating catalogue of spam in propagation that is consulted by
email clients to filter out known spam. Detection is done with statistical and
randomized signatures that efficiently spot mutating spam content. User input
is validated through reputation assignments based on consensus on report and
revoke assertions which in turn is used for computing confidence values
associated with individual signatures.

%prep
%setup -q -n razor-agents-%{version}

%build
perl Makefile.PL
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
