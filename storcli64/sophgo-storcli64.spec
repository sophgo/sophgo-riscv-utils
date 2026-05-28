%define __strip /bin/true

Name:           sophgo-storcli64
Version:        7.1804
Release:        1
Summary:        Broadcom StorCLI utility for Sophgo RISC-V servers (via QEMU emulation)

License:        Proprietary (Broadcom) and GPLv2 (QEMU)
ExclusiveArch:  riscv64
Source0:        %{name}-%{version}.tar.gz

NoSource:       0
URL:            https://www.broadcom.com/products/storage/raid-controllers/storcli
Packager:       Sophgo <support@sophgo.com>

%description
Broadcom StorCLI (v007.1804.0000.0000) management utility for MegaRAID/SAS
controllers, packaged for Sophgo RISC-V servers. Since Broadcom does not ship
RISC-V binaries, this package uses a custom QEMU user-mode emulator (qemu-x86_64,
built for RISC-V with Broadcom RAID ioctl support) to run the x86-64 storcli64
binary transparently. After installation, users can simply run "storcli64" as
they would on an x86 server.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/opt/sophgo/storcli64
mkdir -p %{buildroot}/usr/bin

cp -p qemu-x86_64 %{buildroot}/opt/sophgo/storcli64/qemu-x86_64
cp -p storcli64.real %{buildroot}/opt/sophgo/storcli64/storcli64.real
cp -p storcli64.sh %{buildroot}/usr/bin/storcli64

%files
%defattr(-,root,root,-)
/opt/sophgo/storcli64/qemu-x86_64
/opt/sophgo/storcli64/storcli64.real
/usr/bin/storcli64