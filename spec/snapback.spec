Name: snapback
Version: 0.2.0
Release: 1%{?dist}
Summary: Snapshot & backup btrfs subvolumes

License: MIT
URL: https://github.com/jcrd/snapback
Source0: https://github.com/jcrd/snapback/archive/v0.2.0.tar.gz

BuildArch: noarch

BuildRequires: make

Requires: bash
Requires: btrfs-progs
Requires: coreutils
Requires: gawk
Requires: iniq >= 0.3.0

%global debug_package %{nil}

%description
snapback snapshots and backs up btrfs subvolume daily.

%prep
%setup

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%files
%license LICENSE
%doc README.md
/usr/bin/%{name}
/usr/lib/systemd/user/snapback.service
/usr/lib/systemd/user/snapback.timer

%changelog
* Sun Jun 26 2022 James Reed <james@twiddlingbits.net> - 0.2.0-1
- Release v0.2.0

* Sat Jun  4 2022 James Reed <james@twiddlingbits.net> - 0.1.3-1
- Release v0.1.3

* Sun May 22 2022 James Reed <james@twiddlingbits.net> - 0.1.2-1
- Release v0.1.2

* Sun Dec 19 2021 James Reed <james@twiddlingbits.net> - 0.1.1-1
- Release v0.1.1

* Sun Sep  5 2021 James Reed <james@twiddlingbits.net> - 0.1.0-2
- Add `make` build requirement
- Add `btrfs-progs` runtime requirement

* Sun Sep  5 2021 James Reed <james@twiddlingbits.net> - 0.1.0-1
- Release v0.1.0
