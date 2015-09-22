%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Classic pen and paper game
Name:		bovo
Version:	15.08.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://games.kde.org/game.php?game=bovo
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)

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
%{_datadir}/appdata/bovo.appdata.xml
%{_datadir}/kxmlgui5/bovo

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
