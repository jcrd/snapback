Name: snapback
Version: 0.1.0
Release: 2%{?dist}
Summary: Backup btrfs subvolume snapshots

License: MIT
URL: https://github.com/jcrd/snapback
Source0: https://github.com/jcrd/snapback/archive/v0.1.0.tar.gz

BuildArch: noarch

BuildRequires: make

Requires: bash
Requires: btrfs-progs
Requires: coreutils
Requires: iniq >= 0.3.0

%global debug_package %{nil}

%description
snapback creates and backs up snapshots of btrfs subvolumes daily.

%prep
%setup

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%files
%license LICENSE
%doc README.md
%config(noreplace) /etc/snapback.conf
/usr/bin/%{name}
/usr/lib/systemd/system/snapback.service
/usr/lib/systemd/system/snapback.timer

%changelog
* Sun Sep  5 2021 James Reed <james@twiddlingbits.net> - 0.1.0-2
- Add `make` build requirement
- Add `btrfs-progs` runtime requirement

* Sun Sep  5 2021 James Reed <james@twiddlingbits.net> - 0.1.0-1
- Release v0.1.0
