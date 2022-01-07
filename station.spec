%define snapshot 20220107

Name:		station
Version:	2.1.1
Release:	%{?snapshot:0.%{snapshot}.}1
URL:		https://invent.kde.org/maui/station/
Source0:	https://invent.kde.org/maui/station/-/archive/%{?snapshot:master/station-master.tar.bz2#/station-%{snapshot}}%{!?snapshot:v%{version}/station-v%{version}}.tar.bz2
Group:		Applications/Productivity
Summary:	Terminal for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KIO)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(MauiKit)
BuildRequires:  qml(QMLTermWidget)

Requires: qmltermwidget

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

%files
%{_bindir}/station
%{_datadir}/applications/org.kde.station.desktop
%{_datadir}/icons/hicolor/scalable/apps/station.svg
