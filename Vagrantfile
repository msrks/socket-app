# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "server" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "server"
    node.vm.network :private_network, ip: "192.168.77.100"
  end
  config.vm.define "client1" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "client1"
    node.vm.network :private_network, ip: "192.168.77.101"
  end
  config.vm.define "client2" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "client2"
    node.vm.network :private_network, ip: "192.168.77.102"
  end
  config.vm.define "client3" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "client3"
    node.vm.network :private_network, ip: "192.168.77.103"
  end
#  config.vm.provision "ansible" do |ansible|
#    ansible.playbook = "provisioning/playbook.yml"
#    ansible.inventory_path = "provisioning/hosts"
#    ansible.limit = 'all'
#  end
end
