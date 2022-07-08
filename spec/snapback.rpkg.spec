Name: {{{ git_cwd_name name="snapback" }}}
Version: {{{ git_cwd_version lead="$(git tag | sed -n 's/^v//p' | sort --version-sort -r | head -n1)" }}}
Release: 1%{?dist}
Summary: Snapshot & backup btrfs subvolumes

License: MIT
URL: https://github.com/jcrd/snapback
VCS: {{{ git_cwd_vcs }}}
Source0: {{{ git_cwd_pack }}}

BuildArch: noarch

BuildRequires: make

Requires: bash
Requires: btrfs-progs
Requires: coreutils
Requires: findutils
Requires: gawk
Requires: iniq >= 0.3.0

%global debug_package %{nil}

%description
snapback snapshots and backs up btrfs subvolume daily.

%prep
{{{ git_cwd_setup_macro }}}

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
{{{ git_cwd_changelog }}}
