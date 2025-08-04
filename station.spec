#define snapshot 20220107

Name:		station
Version:	4.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
URL:		https://invent.kde.org/maui/station/
Source0:	https://invent.kde.org/maui/station/-/archive/%{?snapshot:master/station-master.tar.bz2#/station-%{snapshot}}%{!?snapshot:v%{version}/maui-station-v%{version}}.tar.bz2
Group:		Applications/Productivity/Maui
Summary:	Terminal for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(MauiKit4)
#BuildRequires:  qml(QMLTermWidget)
BuildRequires:	cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTerminal4)

Requires: qmltermwidget
Requires: qml(org.mauikit.terminal)

%description
Terminal for Plasma Mobile

%prep
%autosetup -p1 -n maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
#mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
#cp src/assets/station.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/maui-station.svg

%find_lang station

%files -f station.lang
%{_bindir}/station
%{_datadir}/applications/org.kde.station.desktop
%{_datadir}/icons/hicolor/scalable/apps/station.svg
%{_datadir}/metainfo/org.kde.station.appdata.xml
