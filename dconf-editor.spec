Summary:	Configuration editor for dconf
Summary(pl.UTF-8):	Edytor konfiguracji dla dconf
Name:		dconf-editor
Version:	45.0.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/dconf-editor/45/%{name}-%{version}.tar.xz
# Source0-md5:	82b2f5d396e95757ad7eaf89c82decd6
Patch0:		no-schema-upate-cache-compile.patch
URL:		https://wiki.gnome.org/Projects/dconf
BuildRequires:	dconf-devel >= 0.26.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gtk+3-devel >= 3.22.27
BuildRequires:	libhandy1-devel >= 1.6
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.40.0
BuildRequires:	vala-dconf >= 0.26.1
BuildRequires:	vala-libhandy1 >= 1.6
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.56.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	dconf >= 0.26.1
Requires:	glib2 >= 1:2.56.0
Requires:	gtk+3 >= 3.22.27
Requires:	hicolor-icon-theme
Requires:	libhandy1 >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dconf-editor allows you to browse and modify dconf database.

%description -l pl.UTF-8
dconf-editor pozwala na przeglądanie i modyfikowanie bazy dconf.

%package -n bash-completion-dconf-editor
Summary:	bash-completion for dconf-editor
Summary(pl.UTF-8):	Bashowe uzupełnianie nazw dla narzędzia dconf-editor
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-dconf-editor
bash-completion for dconf-editor..

%description -n bash-completion-dconf-editor -l pl.UTF-8
Bashowe uzupełnianie nazw dla narzędzia dconf-editor.

%prep
%setup -q
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang dconf-editor

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f dconf-editor.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/dconf-editor
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
%{_desktopdir}/ca.desrt.dconf-editor.desktop
%{_iconsdir}/hicolor/scalable/actions/ca.desrt.dconf-editor*-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/ca.desrt.dconf-editor.svg
%{_iconsdir}/hicolor/scalable/apps/ca.desrt.dconf-editor.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/ca.desrt.dconf-editor-symbolic.svg
%{_mandir}/man1/dconf-editor.1*

%files -n bash-completion-dconf-editor
%defattr(644,root,root,755)
%{bash_compdir}/dconf-editor
