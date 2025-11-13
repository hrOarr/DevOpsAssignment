# Vagrantfile for 3 App Servers + 1 Reverse Proxy (Ubuntu 24.04)
Vagrant.configure("2") do |config|
  # Base box
  config.vm.box = "alvistack/ubuntu-24.04"

  # Default provider settings
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
    vb.cpus = 1
  end

  # ---------- APP SERVERS ----------
  (1..3).each do |i|
    config.vm.define "vm-app#{i}" do |app|
      app.vm.hostname = "vm-app#{i}"
      app.vm.network "private_network", ip: "192.168.123.1#{i}", name: "vboxnet0"

      # Provider-specific settings for each app VM
      app.vm.provider "virtualbox" do |vb|
        vb.name = "vm-app#{i}"
        vb.memory = 2048     # 2GB RAM
        vb.cpus = 2          # 2 CPUs
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--vram", "16"]
      end
    end
  end

  # ---------- REVERSE PROXY ----------
  config.vm.define "vm-proxy" do |proxy|
    proxy.vm.hostname = "vm-proxy"
    proxy.vm.network "private_network", ip: "192.168.123.14", name: "vboxnet0"

    proxy.vm.provider "virtualbox" do |vb|
      vb.name = "vm-proxy"
      vb.memory = 1024     # 1GB RAM
      vb.cpus = 1
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--vram", "16"]
    end
  end

  # ---------- SHARED SETTINGS ----------
  # Use the default insecure key for SSH unless overridden
  config.ssh.insert_key = false
  # Optional: synced folder
  # config.vm.synced_folder ".", "/vagrant", disabled: true
end

