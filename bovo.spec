%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Classic pen and paper game
Name:		bovo
Version:	15.12.0
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://games.kde.org/game.php?game=bovo
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Bovo is a Gomoku like game for two players, where the opponents alternate in
placing their respective pictogram on the game board. (Also known as: Connect
Five, Five in a row, X and O, Naughts and Crosses)

%files
%{_bindir}/bovo
%{_datadir}/applications/org.kde.bovo.desktop
%{_datadir}/bovo
%{_docdir}/*/*/bovo
%{_iconsdir}/hicolor/*/apps/bovo.*
%{_datadir}/appdata/org.kde.bovo.appdata.xml
%{_datadir}/kxmlgui5/bovo

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
