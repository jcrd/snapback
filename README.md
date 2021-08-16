# snapback

snapback creates and backs up `btrfs` subvolume snapshots daily using a
**systemd** timer.

## Usage

```
usage: snapback [-hrv]

Enable with `systemctl enable snapback.timer`.

options:
    -h  Show help message
    -r  Remove subvolumes and backups
    -v  Show version
```

## Configuration

Sections in the configuration file _/etc/snapback.conf_ are names of subvolumes.
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
