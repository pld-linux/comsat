Summary:	A mail checker client and comsat mail checking server
Summary(de):	Biff-Mail-Checker-Client und comsat-Mail-Checking-Server
Summary(es):	Programa para buscar e-mail en un servidor comsat
Summary(fr):	Le client de notification de courrier Biff et le serveur de notification de courrier comsat
Summary(pl):	Klient i serwer powiadamiania o nadchodz±cej poczcie
Summary(pt_BR):	Um programa para checar e-mail e um servidor comsat
Summary(ru):	ëÌÉÅÎÔ É ÓÅÒ×ÅÒ ÄÌÑ ÐÒÏ×ÅÒËÉ ÎÁÌÉÞÉÑ ÐÏÞÔÙ
Summary(tr):	Ýleti olup olmadýðýný denetleyen istemci ve sunucular
Name:		comsat
Version:	0.17
Release:	7
License:	BSD
Group:		Networking/Daemons
Source0:	ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/biff+%{name}-%{version}.tar.gz
# Source0-md5:	0e366384b0ffc7d4f748713a6359e089
Source1:	%{name}.inetd
Provides:	biff
Prereq:		rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	biff
Obsoletes:	biff+comsat

%description
The biff client and comsat server are an antiquated method of
asynchronous mail notification. Although they are still supported,
most users use their shell's MAIL variable (or csh shell's mail
variable) to check for mail, or a dedicated application like xbiff or
xmailbox. If the comsat service is not enabled, biff won't work and
you'll need to use either the MAIL or mail variable.

%description -l de
biff-Client und comsat-Server sind ein veraltetes Verfahren zur
asynchronen Mail-Benachrichtigung. Obwohl es noch unterstützt wird,
verwenden die meisten Benutzer die MAIL-Variable der Shell (bzw.
'mail' unter csh-Variationen), oder eine spezielle Anwendung wie xbiff
or xmailbox, um neue Mail-Nachrichten abzufragen.

%description -l es
Cliente biff y servidor comsat son métodos anticuados para recibir y
enviar notificaciones asíncronas de nuevos mensajes. A pesar de que
aún se soportan, la mayoría de los usuarios usa sus variables de
ambiente MAIL (el mail bajo variante de csh) para verificar la llegada
de nuevos mensajes, o una aplicación dedicada tal como xbiff o
xmailbox.

%description -l fr
Le client biff et le serveur comsat servent à l'antique notification
asynchrone de mail. Bien qu'ils soient toujours supportés, beaucoup
d'utilisateurs utilisent les variables MAIL du shell ( ou mail sous
les variantes csh), pour se tenir au courant du mail, ou des
applications dédiés comme xbiff ou xmailbox.

%description -l pl
Klient biff oraz serwer comsat to przestarza³a metoda asynchronicznego
powiadamianiu o nadchodz±cej poczcie. Chcia¿ wci±¿ siê je obs³uguje,
wiêkszo¶æ u¿ytkowników ustawia w tym celu zmienn± ¶rodowiskow± MAIL
(lub mail w csh i klonach) lub u¿ywa oddzielnej aplikacji takiej jak
xbiff albo xmailbox.

%description -l pt_BR
O cliente biff e o servidor comsat são métodos antiquados para receber
e enviar notificações assíncronas de novas mensagens. Embora eles
ainda sejam suportados, a maioria dos usuários usa suas variáveis de
ambiente MAIL (ou mail sob variante de csh) para verificar a chegada
de novas mensagens, ou uma aplicação dedicada tal como xbiff ou
xmailbox.

%description -l ru
ëÌÉÅÎÔ biff É ÓÅÒ×ÅÒ comsat - ÜÔÏ ÁÎÔÉË×ÁÒÎÙÊ ÍÅÔÏÄ ÁÓÉÎÈÒÏÎÎÏÇÏ
ÉÚ×ÅÝÅÎÉÑ Ï ÐÒÉÈÏÄÅ ÐÏÞÔÙ. èÏÔÑ ÏÎÉ ×ÓÅ ÅÝÅ ÐÏÄÄÅÒÖÉ×ÁÀÔÓÑ,
ÂÏÌØÛÉÎÓÔ×Ï ÐÏÌØÚÏ×ÁÔÅÌÅÊ ÉÓÐÏÌØÚÕÀÔ ÄÌÑ ÐÒÏ×ÅÒËÉ ÎÁÌÉÞÉÑ ÐÏÞÔÙ
ÐÅÒÅÍÅÎÎÕÀ ÏËÒÕÖÅÎÉÑ MAIL (ÉÌÉ mail ÄÌÑ csh) Ó×ÏÅÇÏ ÛÅÌÌÁ ÉÌÉ
ÓÐÅÃÉÁÌØÎÙÅ ÐÒÏÇÒÁÍÍÙ, ÔÁËÉÅ ËÁË xbiff ÉÌÉ xmailbox.

%description -l tr
biff istemcisi ve comsat sunucusu, eski bir mektup bildirme yöntemini
gerçeklerler. Halen desteklenmelerine karþýn, pek çok kullanýcý,
mektup olup olmadýðýný kontrol etmek için ya bir kabuk deðiþkeni olan
MAIL deðiþkenini (csh kabuðunda mail deðiþkenine karþýlýk gelir) ya da
xbiff, xmailbox gibi uygulamalarý kullanýr.

%prep
%setup -q -n biff+comsat-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--with-c-compiler=%{__cc}

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

install biff/biff $RPM_BUILD_ROOT%{_bindir}
install biff/biff.1 $RPM_BUILD_ROOT%{_mandir}/man1
install comsat/comsat $RPM_BUILD_ROOT%{_sbindir}/in.comsat
install comsat/comsat.8 $RPM_BUILD_ROOT%{_mandir}/man8

echo ".so comsat.8" >$RPM_BUILD_ROOT%{_mandir}/man8/in.comsat.8

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/comsat

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/comsat
%attr(755,root,root) %{_bindir}/biff
%attr(755,root,root) %{_sbindir}/in.comsat
%{_mandir}/man[18]/*
