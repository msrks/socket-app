# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "server" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "server"
    node.vm.network :private_network, ip: "192.168.88.101"
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/site.yml"
      ansible.inventory_path = "provisioning/hosts"
      ansible.limit = 'all'
  end

  config.vm.define "client" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "client"
    node.vm.network :private_network, ip: "192.168.88.102"
  end
end
