%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Classic pen and paper game
Name:		bovo
Version:	22.04.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://games.kde.org/game.php?game=bovo
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)

%description
Bovo is a Gomoku like game for two players, where the opponents alternate in
placing their respective pictogram on the game board. (Also known as: Connect
Five, Five in a row, X and O, Naughts and Crosses).

%files -f %{name}.lang
%{_bindir}/bovo
%{_datadir}/applications/org.kde.bovo.desktop
%{_datadir}/bovo
%{_datadir}/icons/hicolor/*/apps/bovo.*
%{_datadir}/metainfo/org.kde.bovo.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
