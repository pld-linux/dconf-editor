Summary:	Configuration editor for dconf
Summary(pl.UTF-8):	Edytor konfiguracji dla dconf
Name:		dconf-editor
Version:	3.30.2
Release:	1
License:	GPL 3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/dconf-editor/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	5db3d67478c198504167143e069ebab9
URL:		http://www.gnome.org/
BuildRequires:	appstream-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gtk+3-devel >= 3.22.27
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.41.0
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.40.0
BuildRequires:	vala-dconf >= 0.26.1
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	dconf >= 0.26.1
Requires:	glib2 >= 1:2.56.0
Requires:	gtk+3 >= 3.22.27
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dconf-editor allows you to browse and modify dconf database.

%description -l pl.UTF-8
dconf-editor pozwala na przeglądanie i modyfikowanie bazy dconf.

%package -n bash-completion-dconf-editor
Summary:	bash-completion for dconf-editor
Summary(pl.UTF-8):	Bashowe uzupełnianie nazw dla narzędzia dconf-editor
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-dconf-editor
bash-completion for dconf-editor..

%description -n bash-completion-dconf-editor -l pl.UTF-8
Bashowe uzupełnianie nazw dla narzędzia dconf-editor.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang dconf-editor

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f dconf-editor.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/dconf-editor
%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_desktopdir}/ca.desrt.dconf-editor.desktop
%{_iconsdir}/hicolor/*/apps/ca.desrt.dconf-editor.png
%{_iconsdir}/hicolor/scalable/apps/ca.desrt.dconf-editor-symbolic.svg
%{_mandir}/man1/dconf-editor.1*

%files -n bash-completion-dconf-editor
%defattr(644,root,root,755)
%{bash_compdir}/dconf-editor
