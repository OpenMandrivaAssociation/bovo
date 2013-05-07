Name:		bovo
Version:	4.10.3
Release:	1
Epoch:		1
Summary:	Classic pen and paper game
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://games.kde.org/game.php?game=bovo
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Bovo is a Gomoku (from Japanese 五目並べ - lit. "five points") like game for two
players, where the opponents alternate in placing their respective pictogram on
the game board. (Also known as: Connect Five, Five in a row, X and O, Naughts
and Crosses)

%files
%{_kde_bindir}/bovo
%{_kde_applicationsdir}/bovo.desktop
%{_kde_appsdir}/bovo
%{_kde_docdir}/*/*/bovo
%{_kde_iconsdir}/hicolor/*/apps/bovo.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

