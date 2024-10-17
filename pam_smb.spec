%define name	pam_smb
%define version	1.1.7
%define release	6

Summary:	SMB Pluggable Authentication Module
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.samba.org/pub/samba/pam_smb/pam_smb-%{version}.tar.bz2
URL:		https://www.csn.ul.ie/~airlied/pam_smb/
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.7-5mdv2010.0
+ Revision: 430233
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.7-4mdv2009.0
+ Revision: 241134
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.1.7-2mdv2008.0
+ Revision: 70135
- use %%mkrel


* Mon Jan 06 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.1.7-1mdk
- 1.1.7 (security issue)

* Mon Jan 06 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.1.6-4mdk
- Rebuild

* Wed Apr 17 2002 <bgmilne@cae.co.za> 1.1.6-3mdk
- s/Copyright/License

* Thu Oct 04 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.1.6-2mdk
- specfile cleanups, macros

* Sun Jul 29 2001 Buchan Milne <bgmilne@cae.co.za> 1.1.6-1mdk
- Mandrake package, added requires and buildrequires

* Sun Sep 10 2000 Carlo Marcelo Arenas Belon <carenas@chasqui.lared.net.pe>
- making SPEC LFS aware
- update to 1.1.6 (security recommended)

* Wed Sep 08 1999 Carlo Marcelo Arenas Belon <carenas@chasqui.lared.net.pe>
- first spec, most ideas taken from pam_ldap

