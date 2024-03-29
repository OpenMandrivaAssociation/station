#define snapshot 20220107

Name:		station
Version:	3.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
URL:		https://invent.kde.org/maui/station/
Source0:	https://invent.kde.org/maui/station/-/archive/%{?snapshot:master/station-master.tar.bz2#/station-%{snapshot}}%{!?snapshot:v%{version}/station-v%{version}}.tar.bz2
Group:		Applications/Productivity/Maui
Summary:	Terminal for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  qml(QMLTermWidget)
BuildRequires:	cmake(MauiKitFileBrowsing3)
BuildRequires:  cmake(MauiKitTerminal3)

Requires: qmltermwidget
Requires: qml(org.mauikit.terminal)

%description
Terminal for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
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
