# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version '>= 1.6.5'

Vagrant.configure(2) do |config|

  config.vm.box = 'ubuntu/precise64'

  config.vm.define 'docker-host' do |app|
    # Disable the default synced folder
    app.vm.synced_folder '.', '/vagrant', :disabled => true
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'docker-host.yml'
    ansible.host_key_checking = false
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'iamproxy.yml'
    ansible.host_key_checking = false
    ansible.extra_vars = {
      AWS_ACCESS_KEY_ID: ENV['AWS_ACCESS_KEY_ID'],
      AWS_SECRET_ACCESS_KEY: ENV['AWS_SECRET_ACCESS_KEY']
    }
  end

  # The following line terminates all ssh connections. Therefore
  # Vagrant will be forced to reconnect.
  # That's a workaround to have the docker command in the PATH and
  # add Vagrant to the docker group by logging in/out
  config.vm.provision 'shell', :inline =>
    "ps aux | grep 'sshd:' | awk '{print $2}' | xargs kill"

end
