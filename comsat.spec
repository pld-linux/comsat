Summary:	A mail checker client and comsat mail checking server
Summary(pl):	Klient i serwer powiadamiania o nadchodz±cej poczcie
Name:		comsat
Version:	0.10
Release:	22
License:	BSD
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/finger/biff+%{name}-%{version}.tar.gz
Source1:	%{name}.inetd
Patch0:		biff+%{name}-0.10-misc.patch
Patch1:		biff+%{name}-0.10-nobr.patch
Obsoletes:	biff
Provides:	biff
Prereq:		rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The biff client and comsat server are an antiquated method of
asynchronous mail notification. Although they are still supported,
most users use their shell's MAIL variable (or csh shell's mail
variable) to check for mail, or a dedicated application like xbiff or
xmailbox. If the comsat service is not enabled, biff won't work and
you'll need to use either the MAIL or mail variable.

You may want to install biff if you'd like to be notified when mail
arrives. However, you should probably check out the more modern
methodologies of mail notification (xbiff or xmailbox) instead.

%description -l pl
Klient biff oraz serwer comsat to przestarza³a metoda asynchronicznego
powiadamianiu o nadchodz±cej poczcie. Chcia¿ wci±¿ siê je obs³uguje,
wiêkszo¶æ u¿ytkowników ustawia w tym celu zmienn± ¶rodowiskow± MAIL
(lub mail w csh i klonach) lub u¿ywa oddzielnej aplikacji takiej jak
xbiff albo xmailbox.

%prep
%setup -q -n biff+comsat-0.10
%patch0 -p1
%patch1 -p1

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install INSTALLROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/comsat

%clean
rm -rf $RPM_BUILD_ROOT

%post
%rc_inetd_post

%postun
%rc_inetd_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/biff
%attr(755,root,root) %{_sbindir}/in.comsat
%{_mandir}/man1/biff.1*
%{_mandir}/man8/in.comsat.8*
%{_mandir}/man8/comsat.8*
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/comsat
