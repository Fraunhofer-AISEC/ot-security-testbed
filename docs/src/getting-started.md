## Getting Started

The script `testbed.py` provides functionality such as setting dependencies (Docker, etc.),
building the containers and starting/stopping.

### Installation:

The installation script supports Debian, Ubuntu and ArchLinux.
It is essentially a wrapper around the [official instructions provided by Docker.](https://docs.docker.com/engine/)
The flag `--dont-ask-sudo` can be used to skip the script from asking everytime before running a sudo command.

```shell
./testbed.py --install debian # options are 'debian', 'ubuntu' and 'arch'
```

### Building, Starting and Stopping the testbed

You can build the local version and start it the following way:

```shell
./testbed.py --build local
./testbed.py --start local -d
```

You can replace `local` with one of `{local, prod, dev}`,
however most of the time you will want the local version.
For more information [look at the version chapter.](./versions.md)

If you want to stop it again you can with:

```shell
./testbed.py --stop
```