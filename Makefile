VERSIONCMD = git describe --dirty --tags --always 2> /dev/null
VERSION := $(shell $(VERSIONCMD) || cat VERSION)

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
LIBPREFIX ?= $(PREFIX)/lib

all: snapback

snapback: snapback.in
	sed -e "s/@VERSION/$(VERSION)/" snapback.in > snapback
	chmod +x snapback

install:
	mkdir -p $(DESTDIR)$(BINPREFIX)
	cp -p snapback $(DESTDIR)$(BINPREFIX)
	mkdir -p $(DESTDIR)$(LIBPREFIX)/systemd/user
	cp -p systemd/snapback.service $(DESTDIR)$(LIBPREFIX)/systemd/user
	cp -p systemd/snapback.timer $(DESTDIR)$(LIBPREFIX)/systemd/user

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/snapback
	rm -f $(DESTDIR)$(LIBPREFIX)/systemd/user/snapback.service
	rm -f $(DESTDIR)$(LIBPREFIX)/systemd/user/snapback.timer

clean:
	rm -f snapback

.PHONY: all install uninstall clean
