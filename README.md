# snapback

snapback snapshots and backs up `btrfs` subvolume daily using a
**systemd** timer.

## Packages

* **RPM** package available from [copr][copr]. [![Copr build status](https://copr.fedorainfracloud.org/coprs/jcrd/snapback/package/snapback/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jcrd/snapback/package/snapback/)

  Install with:
  ```
  dnf copr enable jcrd/snapback
  dnf install snapback
  ```

[copr]: https://copr.fedorainfracloud.org/coprs/jcrd/snapback/

## Usage

```
usage: snapback [-hrv]

Enable with `systemctl --user enable snapback.timer`.

options:
    -h  Show help message
    -r  Remove subvolumes and backups
    -v  Show version
```

## Configuration

Sections in the configuration file _~/.config/snapback/snapback.conf_ are names
of subvolumes relative to the user's home directory.

For example:

```ini
[projects]
backup=/mnt/backup
keep_snapshots=7
keep_backups=31
```

In the above configuration file, the section denotes a subvolume at `~/projects`.

The available options are shown below:

* `backup=`

The directory on a `btrfs` filesystem to which the subvolume snapshots are to be
backed up.

* `keep_snapshots=`

The number of subvolume snapshots to keep.

* `keep_backups=`

The number of subvolume snapshot backups to keep. Requires the `backup=` option
to be specified.

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).
