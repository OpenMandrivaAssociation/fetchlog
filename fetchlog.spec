Summary:	Fetch and convert new messages of a logfile
Name:		fetchlog
Version:	1.4
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/fetchlog/
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
%doc CHANGES LICENSE README README.Nagios README.SNMP
%{_bindir}/*
%{_mandir}/man1/*


