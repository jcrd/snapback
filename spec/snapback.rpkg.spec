Name: {{{ git_name name="snapback" }}}
Version: {{{ git_version lead="$(git tag | sed -n 's/^v//p' | sort --version-sort -r | head -n1)" }}}
Release: 1%{?dist}
Summary: Backup btrfs subvolume snapshots

License: MIT
URL: https://github.com/jcrd/snapback
VCS: {{{ git_vcs }}}
Source0: {{{ git_pack }}}

BuildArch: noarch

Requires: bash
Requires: coreutils
Requires: iniq >= 0.3.0

%global debug_package %{nil}

%description
snapback creates and backs up snapshots of btrfs subvolumes daily.

%prep
{{{ git_setup_macro }}}

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
{{{ git_changelog }}}
