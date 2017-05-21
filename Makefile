BINDIR = /usr/bin

install:
	mkdir -p $(DESTDIR)$(BINDIR)
	install -m 0755 batmon.py $(DESTDIR)$(BINDIR)/batmon.py
	mkdir -p $(DESTDIR)/etc/polkit-1/rules.d/
	install -m 0644 10-hibernate-permission.rules $(DESTDIR)/etc/polkit-1/rules.d/10-hibernate-permission.rules
	mkdir -p $(DESTDIR)/etc/
	test -f $(DESTDIR)/etc/batmon.conf || \
		install -m 0644 batmon.conf $(DESTDIR)/etc/batmon.conf

.PHONY: install

