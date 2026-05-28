.SUFFIXES:
NAME    = sophgo-storcli64
VERSION = 7.1804
RELEASE = 1
ARCH    = riscv64

TARBALL  = $(NAME)-$(VERSION).tar.gz
SPEC     = $(NAME).spec
STAGING  = $(NAME)-$(VERSION)

RPMBUILD = $(CURDIR)/rpmbuild

.PHONY: all rpm srpm clean

all: rpm srpm

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

clean:
	rm -rf $(STAGING) $(TARBALL) $(RPMBUILD)