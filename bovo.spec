#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Classic pen and paper game
Name:		bovo
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://games.kde.org/game.php?game=bovo
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/bovo/-/archive/%{gitbranch}/bovo-%{gitbranchd}.tar.bz2#/bovo-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/bovo-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6SvgWidgets)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)

%rename plamsa6-bovo

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
