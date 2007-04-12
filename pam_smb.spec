%define name	pam_smb
%define version	1.1.7
%define release	1mdk

Summary:	SMB Pluggable Authentication Module
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.samba.org/pub/samba/pam_smb/pam_smb-%{version}.tar.bz2
URL:		http://www.csn.ul.ie/~airlied/pam_smb/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	pam-devel
Requires:	pam

%description 
pam_smb is a PAM module which allows authentication of UNIX users
using an NT/Samba server.

%prep
%setup -q -n pam_smb

%build
%configure
make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_sysconfdir},/lib/security}
install -m 755 pam_smb_auth.so %{buildroot}/lib/security
install -m 644 pam_smb.conf.example %{buildroot}%{_sysconfdir}/pam_smb.conf

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}

%files
%defattr(-,root,root)
/lib/security/pam_smb_auth.so
%config(noreplace) %{_sysconfdir}/pam_smb.conf
%doc CHANGES COPYING README TODO pam_smb.conf.example

