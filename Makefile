BINDIR = /usr/bin

install:
	mkdir -p $(DESTDIR)$(BINDIR)
	install -m 0755 batmon.py $(DESTDIR)$(BINDIR)/batmon.py
	mkdir -p $(DESTDIR)/usr/share/polkit-1/rules.d/
	install -m 0644 batmon.rules $(DESTDIR)/usr/share/polkit-1/rules.d/batmon.rules
	mkdir -p $(DESTDIR)/etc/
	test -f $(DESTDIR)/etc/batmon.conf \
		&& install -m 0644 batmon.conf $(DESTDIR)/etc/batmon.conf.example \
		|| install -m 0644 batmon.conf $(DESTDIR)/etc/batmon.conf
	mkdir -p $(DESTDIR)/usr/lib/systemd/system
	install -m 644 batmon.service $(DESTDIR)/usr/lib/systemd/system/batmon.service
	mkdir -p $(DESTDIR)/usr/lib/tmpfiles.d
	install -m 644 batmon.tmpfiles $(DESTDIR)/usr/lib/tmpfiles.d/batmon.conf

.PHONY: install

