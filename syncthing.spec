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
Version:0.9.5
Release:1.3%{?dist}
Summary:Syncthing
License:MIT
URL:http://syncthing.net/    
Source0:https://github.com/calmh/%{name}/releases/download/v%{version}/%{name}-linux-%{altarch}-v%{version}.tar.gz
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
install -p -m 0755 %{name}-linux-%{altarch}-v%{version}/syncthing %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{S:1} %{buildroot}%{_unitdir}


%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service 

%files
%doc  %{name}-linux-%{altarch}-v%{version}/README.md %{name}-linux-%{altarch}-v%{version}/LICENSE %{name}-linux-%{altarch}-v%{version}/CONTRIBUTORS
%{_bindir}/syncthing
%{_unitdir}/%{name}@.service



%changelog

* Sat Aug 17 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.5-1.3
- Version updated to v0.9.5

* Sat Aug 16 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.4-1.2
- Version updated to v0.9.4

* Mon Jul 28 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.8.21-1.1
- Initial Version

