Summary: A mail checker client and comsat mail checking server.
Name: comsat
Version: 0.10
Release: 22
Copyright: BSD
Group: System Environment/Daemons
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/finger/biff+comsat-0.10.tar.gz
Patch0: biff+comsat-0.10-misc.patch
Patch1: biff+comsat-0.10-nobr.patch
Obsoletes: biff
Provides: biff
Requires: inetd
BuildRoot: /var/tmp/%{name}-root

%description
The biff client and comsat server are an antiquated method of
asynchronous mail notification.  Although they are still supported, most
users use their shell's MAIL variable (or csh shell's mail variable) to
check for mail, or a dedicated application like xbiff or xmailbox.  If
the comsat service is not enabled, biff won't work and you'll need to use
either the MAIL or mail variable.   

You may want to install biff if you'd like to be notified when mail
arrives. However, you should probably check out the more modern
methodologies of mail notification (xbiff or xmailbox) instead.

%prep
%setup -q -n biff+comsat-0.10
%patch0 -p1
%patch1 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/biff
/usr/man/man1/biff.1
/usr/sbin/in.comsat
/usr/man/man8/in.comsat.8
/usr/man/man8/comsat.8
