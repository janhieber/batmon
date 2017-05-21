# Maintainer: Jan Hieber <mail@janhieber.net>

pkgname=batmon
pkgver=r0.0
pkgrel=1
pkgdesc="Lightweight battery monitor (no GUI, multiple batteries)"
url="https://github.com/janhieber/batmon"
arch=(i686 x86_64)
license=(MIT)
depends=(python-psutil python-dbus)
source=("git+https://github.com/janhieber/batmon.git")
sha256sums=('SKIP')

pkgver() {
    cd $pkgname
    printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd "$pkgname"
    make DESTDIR="$pkgdir/" install
}

