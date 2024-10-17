Summary:	Fetch and convert new messages of a logfile
Name:		fetchlog
Version:	1.6
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://sourceforge.net/projects/fetchlog/
Source0:	http://prdownloads.sourceforge.net/fetchlog/%{name}-%{version}.tar.gz

%description
The fetchlog utility displays the last new messages of a logfile
(syslog).  fetchlog is similar like tail but offers some extra
functionality like pattern matching with regular expressions,
output formatting for email, SMS, pager or SNMP tools, etc.

%prep

%setup -q -n %{name}-%{version}

%build

%make CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 fetchlog %{buildroot}%{_bindir}/
install -m0644 fetchlog.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGES README README.Nagios README.SNMP
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Mon May 07 2012 Johnny A. Solbu <solbu@mandriva.org> 1.4-2
+ Revision: 797251
- Don't ship LICENSE file, licence doesn't require it

* Fri Apr 06 2012 Johnny A. Solbu <solbu@mandriva.org> 1.4-1
+ Revision: 789527
- New version

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdv2011.0
+ Revision: 618277
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.2-2mdv2010.0
+ Revision: 437533
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.2-1mdv2009.1
+ Revision: 324629
- New upstream release

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 245103
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0-2mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdv2007.0
+ Revision: 115937
- Import fetchlog

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- rebuild

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-1mdk
- initial mandrake package

