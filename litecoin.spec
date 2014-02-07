Summary:	Litecoin is a peer-to-peer currency
Name:		litecoin
Version:	0.8.3.7
Release:	1
License:	MIT/X11
Group:		Databases
Source0:	https://github.com/litecoin-project/litecoin/archive/v%{version}.tar.gz
Patch0:		berkdb60-litecoin.patch

URL:		http://www.litecoin.org
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	db-devel
BuildRequires:	miniupnpc-devel >= 1.5
BuildRequires:	openssl-devel
BuildRequires:	qrencode-devel

%description
Litecoin is a peer-to-peer currency. Peer-to-peer means that no central
authority issues new money or tracks transactions. These tasks are
managed collectively by the network.

%package qt
Summary:	Qt-based Litecoin Wallet
Group:		Graphical desktop/KDE

%description qt
Qt-based Litecoin Wallet.

%prep
%setup -q
%apply_patches

%build
%qmake_qt4 \
	USE_UPNP=1 \
	USE_DBUS=1 \
	USE_QRCODE=1

%make

%make -C src -f makefile.unix \
	CXX="%{__cxx}" \
	CXXFLAGS="%{optflags}"

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man{1,5},%{_localedir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/kde4/services}

install -m755 src/litecoind %{buildroot}%{_bindir}/litecoind

install litecoin-qt %{buildroot}%{_bindir}
sed -e 's#bitcoin#litecoin#g' contrib/debian/bitcoin-qt.desktop > %{buildroot}%{_desktopdir}/litecoin-qt.desktop
sed -e 's#bitcoin#litecoin#g' contrib/debian/bitcoin-qt.protocol > %{buildroot}%{_datadir}/kde4/services/litecoin-qt.protocol

%files
%defattr(644,root,root,755)
%doc doc/*.txt contrib/debian/examples/bitcoin.conf
%attr(755,root,root) %{_bindir}/litecoind

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/litecoin-qt
%{_datadir}/kde4/services/litecoin-qt.protocol
%{_desktopdir}/litecoin-qt.desktop
