Summary:	Configuration editor for dconf
Summary(pl.UTF-8):	Edytor konfiguracji dla dconf
Name:		dconf-editor
Version:	3.18.2
Release:	1
License:	LGPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/dconf-editor/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	9292d9b96b0d9f87f6589a7d1d0ca388
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.2
BuildRequires:	dconf-devel >= 0.24.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.26.0
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	dconf >= 0.24.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dconf-editor allows you to browse and modify dconf database.

%description -l pl.UTF-8
dconf-editor pozwala na przeglądanie i modyfikowanie bazy dconf.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang dconf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f dconf.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/dconf-editor
%{_datadir}/appdata/ca.desrt.dconf-editor.appdata.xml
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_desktopdir}/ca.desrt.dconf-editor.desktop
%{_iconsdir}/hicolor/*/apps/dconf-editor.png
%{_iconsdir}/hicolor/scalable/apps/dconf-editor-symbolic.svg
%{_mandir}/man1/dconf-editor.1*
