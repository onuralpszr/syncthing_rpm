%global debug_package %{nil}

%ifarch x86_64
%global altarch amd64
%endif
%ifarch %{ix86}
%global altarch 386
%endif
%ifarch %{arm}
%global altarch armv7
%endif

Name:syncthing
Version:0.10.20
Release:1%{?dist}
Summary:Syncthing
License:MIT
URL:http://syncthing.net/    
Source0:https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-linux-%{altarch}-v%{version}.tar.gz
Source1:	syncthing@.service
Source2:	%{name}-linux-386-v%{version}.tar.gz
ExclusiveArch:  x86_64 %{ix86}
BuildRequires:  systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Syncthing replaces Dropbox and BitTorrent Sync with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

%prep
%setup -c

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 -g wheel %{name}-linux-%{altarch}-v%{version}/syncthing %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{S:1} %{buildroot}%{_unitdir}


%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service 

%files
%doc  %{name}-linux-%{altarch}-v%{version}/README.txt %{name}-linux-%{altarch}-v%{version}/LICENSE.txt %{name}-linux-%{altarch}-v%{version}/AUTHORS.txt
%{_bindir}/syncthing
%{_unitdir}/%{name}@.service


%changelog
* Fri Jan 16 2015 Joris Claassen <joris@claassen.co> 0.10.20-6
- Updated for FC21
- Version updated to v0.10.20
- Changed group permissions for auto-updater to work for all users with sudo rights (wheel group)

* Sat Aug 25 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.9-5
- Version updated to v0.9.9
- Readme fixes
- Source folder path fixed

* Sat Aug 25 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.8-4
- Version updated to v0.9.8

* Sat Aug 17 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.5-3
- Version updated to v0.9.5

* Sat Aug 16 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.4-2
- Version updated to v0.9.4

* Mon Jul 28 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.8.21-1
- Initial Version

