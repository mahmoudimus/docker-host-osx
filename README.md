# docker-host

 `docker-host` uses `Vagrant` to provide an experience similar to [boot2docker](http://boot2docker.io/), and serves as a seamless layer for interacting w/ docker through the host operating system.

`docker-host` has a **very simple** ansible playbook called `docker-host.yml` that configures the the docker daemon living in the `docker-host` as well as sets up a seamless private network to interact with the `docker-host` through the host operating system -- OSX and Linux systems are supported only for now.

The main purpose of `docker-host` is to essentially serve a virtual machine that runs the docker daemon. This becomes the basis of an execution environment for all docker images, used in the instructions further below, in which a shared virtual machine executes all the docker images and exposes them via the host machine's command-line client.


## Instructions

### OSX

To get started, on your host system, you need:

- Ansible 1.8.2+
- Vagrant 1.7+
- docker v1.6.0

#### brew commands
- `brew install ansible`
- `brew cask install vagrant`
- `vagrant plugin install nugrant`
- `brew install docker`

### LINUX 

(todo)

## Play

Then, `vagrant up docker-host` - wait until it's done. 

Then, `export DOCKER_HOST=10.2.0.10:2375` (probably should put that in your `${shell}rc` or `${shell}`profile).

To test a successful installation, type in `docker ps` from your host machine cli and you should see:

```bash
mahmoud@gauss:15/04/08,11:09 λ ~ rb:1.9.3-p286
❯❯❯ uname -a                                                                                                                        ⏎
Darwin gauss 14.1.0 Darwin Kernel Version 14.1.0: Thu Feb 26 19:26:47 PST 2015; root:xnu-2782.10.73~1/RELEASE_X86_64 x86_64

mahmoud@gauss:15/04/08,11:09 λ ~ rb:1.9.3-p286
❯❯❯ docker ps
CONTAINER ID        IMAGE                          COMMAND                CREATED             STATUS              PORTS                                                                    NAMES
```

When done provisioning, `docker login` to set credentials.
