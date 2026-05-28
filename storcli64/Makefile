.SUFFIXES:
NAME    = sophgo-storcli64
VERSION = 7.1804
RELEASE = 1
ARCH    = riscv64

TARBALL  = $(NAME)-$(VERSION).tar.gz
SPEC     = $(NAME).spec
STAGING  = $(NAME)-$(VERSION)

RPMBUILD = $(CURDIR)/rpmbuild

DEBSTAGING = $(CURDIR)/debbuild/$(NAME)_$(VERSION)-$(RELEASE)_$(ARCH)
DEB        = $(NAME)_$(VERSION)-$(RELEASE)_$(ARCH).deb
CONTROL    = $(NAME).control

.PHONY: all rpm srpm deb clean

all: rpm srpm deb

$(TARBALL): $(SPEC)
	rm -rf $(STAGING)
	mkdir -p $(STAGING)
	cp $(CURDIR)/qemu-x86_64  $(STAGING)/qemu-x86_64
	cp $(CURDIR)/storcli64    $(STAGING)/storcli64.real
	cp $(CURDIR)/storcli64.sh $(STAGING)/storcli64.sh
	cp $(CURDIR)/$(SPEC)      $(STAGING)/$(SPEC)
	chmod 0755 $(STAGING)/qemu-x86_64
	chmod 0755 $(STAGING)/storcli64.real
	chmod 0755 $(STAGING)/storcli64.sh
	tar czf $(TARBALL) -C $(STAGING) .
	@echo "Created $(TARBALL)"

rpm: $(TARBALL) $(SPEC)
	mkdir -p $(RPMBUILD)/BUILD $(RPMBUILD)/RPMS/$(ARCH) $(RPMBUILD)/SOURCES $(RPMBUILD)/SPECS $(RPMBUILD)/SRPMS
	cp $(TARBALL) $(RPMBUILD)/SOURCES/
	cp $(SPEC)    $(RPMBUILD)/SPECS/
	rpmbuild -bb $(RPMBUILD)/SPECS/$(SPEC) \
		--define '_topdir $(RPMBUILD)' \
		--target $(ARCH)
	@echo "RPM: $(RPMBUILD)/RPMS/$(ARCH)/$(NAME)-$(VERSION)-$(RELEASE).$(ARCH).rpm"

srpm: $(TARBALL) $(SPEC)
	mkdir -p $(RPMBUILD)/BUILD $(RPMBUILD)/RPMS/$(ARCH) $(RPMBUILD)/SOURCES $(RPMBUILD)/SPECS $(RPMBUILD)/SRPMS
	cp $(TARBALL) $(RPMBUILD)/SOURCES/
	cp $(SPEC)    $(RPMBUILD)/SPECS/
	rpmbuild -bs $(RPMBUILD)/SPECS/$(SPEC) \
		--define '_topdir $(RPMBUILD)'
	@echo "SRPM: $(RPMBUILD)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE).src.rpm"

deb:
	rm -rf $(DEBSTAGING)
	mkdir -p $(DEBSTAGING)/DEBIAN
	mkdir -p $(DEBSTAGING)/opt/sophgo/storcli64
	mkdir -p $(DEBSTAGING)/usr/bin
	cp $(CURDIR)/qemu-x86_64  $(DEBSTAGING)/opt/sophgo/storcli64/qemu-x86_64
	cp $(CURDIR)/storcli64     $(DEBSTAGING)/opt/sophgo/storcli64/storcli64.real
	cp $(CURDIR)/storcli64.sh  $(DEBSTAGING)/usr/bin/storcli64
	chmod 0755 $(DEBSTAGING)/opt/sophgo/storcli64/qemu-x86_64
	chmod 0755 $(DEBSTAGING)/opt/sophgo/storcli64/storcli64.real
	chmod 0755 $(DEBSTAGING)/usr/bin/storcli64
	cp $(CURDIR)/$(CONTROL) $(DEBSTAGING)/DEBIAN/control
	dpkg-deb --build $(DEBSTAGING)
	mv $(DEBSTAGING).deb $(CURDIR)/$(DEB)
	@echo "DEB: $(CURDIR)/$(DEB)"

clean:
	rm -rf $(STAGING) $(TARBALL) $(RPMBUILD) $(DEBSTAGING) $(DEB) debbuild