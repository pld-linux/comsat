Summary:	A mail checker client and comsat mail checking server
Summary(de):	Biff-Mail-Checker-Client und comsat-Mail-Checking-Server
Summary(es):	Programa para buscar e-mail en un servidor comsat
Summary(fr):	Le client de notification de courrier Biff et le serveur de notification de courrier comsat
Summary(pl):	Klient i serwer powiadamiania o nadchodz�cej poczcie
Summary(pt_BR):	Um programa para checar e-mail e um servidor comsat
Summary(ru):	������ � ������ ��� �������� ������� �����
Summary(tr):	�leti olup olmad���n� denetleyen istemci ve sunucular
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
asynchronen Mail-Benachrichtigung. Obwohl es noch unterst�tzt wird,
verwenden die meisten Benutzer die MAIL-Variable der Shell (bzw.
'mail' unter csh-Variationen), oder eine spezielle Anwendung wie xbiff
or xmailbox, um neue Mail-Nachrichten abzufragen.

%description -l es
Cliente biff y servidor comsat son m�todos anticuados para recibir y
enviar notificaciones as�ncronas de nuevos mensajes. A pesar de que
a�n se soportan, la mayor�a de los usuarios usa sus variables de
ambiente MAIL (el mail bajo variante de csh) para verificar la llegada
de nuevos mensajes, o una aplicaci�n dedicada tal como xbiff o
xmailbox.

%description -l fr
Le client biff et le serveur comsat servent � l'antique notification
asynchrone de mail. Bien qu'ils soient toujours support�s, beaucoup
d'utilisateurs utilisent les variables MAIL du shell ( ou mail sous
les variantes csh), pour se tenir au courant du mail, ou des
applications d�di�s comme xbiff ou xmailbox.

%description -l pl
Klient biff oraz serwer comsat to przestarza�a metoda asynchronicznego
powiadamianiu o nadchodz�cej poczcie. Chcia� wci�� si� je obs�uguje,
wi�kszo�� u�ytkownik�w ustawia w tym celu zmienn� �rodowiskow� MAIL
(lub mail w csh i klonach) lub u�ywa oddzielnej aplikacji takiej jak
xbiff albo xmailbox.

%description -l pt_BR
O cliente biff e o servidor comsat s�o m�todos antiquados para receber
e enviar notifica��es ass�ncronas de novas mensagens. Embora eles
ainda sejam suportados, a maioria dos usu�rios usa suas vari�veis de
ambiente MAIL (ou mail sob variante de csh) para verificar a chegada
de novas mensagens, ou uma aplica��o dedicada tal como xbiff ou
xmailbox.

%description -l ru
������ biff � ������ comsat - ��� ����������� ����� ������������
��������� � ������� �����. ���� ��� ��� ��� ��������������,
����������� ������������� ���������� ��� �������� ������� �����
���������� ��������� MAIL (��� mail ��� csh) ������ ����� ���
����������� ���������, ����� ��� xbiff ��� xmailbox.

%description -l tr
biff istemcisi ve comsat sunucusu, eski bir mektup bildirme y�ntemini
ger�eklerler. Halen desteklenmelerine kar��n, pek �ok kullan�c�,
mektup olup olmad���n� kontrol etmek i�in ya bir kabuk de�i�keni olan
MAIL de�i�kenini (csh kabu�unda mail de�i�kenine kar��l�k gelir) ya da
xbiff, xmailbox gibi uygulamalar� kullan�r.

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
