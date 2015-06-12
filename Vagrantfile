# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version '>= 1.6.5'

BRIDGE_NETWORK = '10.2.0.10'
BRIDGE_NETMASK = '255.255.0.0'

Vagrant.configure(2) do |config|

  # sudo route -n add -net 172.17.0.0 10.2.0.10
  # sudo route -nv add -net 192.168.59 -interface vboxnet1
  # # OSX
  # $> sudo route -n add -net 172.17.0.0 10.2.0.10
  # Linux (untested)
  # $> sudo route -net 172.17.0.0 netmask 255.255.0.0 gw 10.2.0.10

  config.vm.define 'docker-host', {:primary => true} do |dh|
    dh.vm.box = 'ubuntu/trusty64'
    # http://stackoverflow.com/a/19758886/133514
    # Disable the default synced folder
    dh.vm.synced_folder '.', '/vagrant', :disabled => true
    dh.vm.network :private_network, :ip => BRIDGE_NETWORK, :netmask => BRIDGE_NETMASK
    dh.vm.network "forwarded_port", :guest => 2375, :host => 2375
    dh.vm.provider :virtualbox do |vb|
      # The --nicpromisc2 translates to Promiscuous mode for nic2, where nic2 -> eth1.
      # So --nocpromisc3 would change that setting for eth2, etc.
       vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
    end

    dh.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'docker-host.yml'
      ansible.host_key_checking = false
      ansible.verbose = 'vvv'
      ansible.extra_vars = {
          :bridge_network => BRIDGE_NETWORK,
          :bridge_netmask => BRIDGE_NETMASK,
          :local_user => ENV['USER']
      }
    end

  end

  config.vm.define 'centos-docker-host' do |rhdh|
    rhdh.vm.box = 'chef/centos-6.5'
    rhdh.vm.synced_folder '.', '/vagrant', :disabled => true
    rhdh.vm.network :private_network, :ip => BRIDGE_NETWORK, :netmask => BRIDGE_NETMASK
    rhdh.vm.network "forwarded_port", :guest => 2375, :host => 2375
    rhdh.vm.provider :virtualbox do |vb|
      # The --nicpromisc2 translates to Promiscuous mode for nic2, where nic2 -> eth1.
      # So --nocpromisc3 would change that setting for eth2, etc.
       vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
    end

    rhdh.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'docker-host.yml'
      ansible.host_key_checking = false
      ansible.extra_vars = {
          :bridge_network => BRIDGE_NETWORK,
          :bridge_netmask => BRIDGE_NETMASK,
          :local_user => ENV['USER']
      }
    end
    #
    # rhdh.vm.provision 'ansible' do |ansible|
    #   ansible.playbook = 'emulate-amazon-linux.yml'
    #   ansible.host_key_checking = false
    #   ansible.extra_vars = {
    #       :AWS_ACCESS_KEY_ID => ENV['AWS_ACCESS_KEY_ID'],
    #       :AWS_SECRET_ACCESS_KEY => ENV['AWS_SECRET_ACCESS_KEY']
    #   }
    # end
  end

  # config.vm.provision 'ansible' do |ansible|
  #   ansible.playbook = 'iamproxy.yml'
  #   ansible.host_key_checking = false
  #   ansible.extra_vars = {
  #     :AWS_ACCESS_KEY_ID => ENV['AWS_ACCESS_KEY_ID'],
  #     :AWS_SECRET_ACCESS_KEY => ENV['AWS_SECRET_ACCESS_KEY']
  #   }
  # end

  # The following line terminates all ssh connections. Therefore
  # Vagrant will be forced to reconnect.
  # That's a workaround to have the docker command in the PATH and
  # add Vagrant to the docker group by logging in/out
  config.vm.provision 'shell', :inline =>
    "ps aux | grep 'sshd:' | awk '{print $2}' | xargs kill"

end
