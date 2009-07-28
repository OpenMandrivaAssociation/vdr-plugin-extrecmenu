
%define plugin	extrecmenu
%define name	vdr-plugin-%plugin
%define version	1.1
%define rel	5

Summary:	VDR plugin: Extended recordings menu
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://martins-kabuff.de/extrecmenu_en.html
Source:		http://martins-kabuff.de/download/vdr-%plugin-%version.tgz
Patch0:		extrecmenu-1.1-i18n-1.6.patch
Patch1:		extrecmenu-const-char-gcc4.4.patch
Patch2:		extrecmenu-graphtft.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin provides a recordings menu enhanced with the possibility to
rename or move recordings and directories. The display of recording date, time
and length is configurable. Sorting by name or date is selectable for each
directory. If you use the PIN-plugin, the replay and editing of recordings is
protected. The plugin also handles archive dvds of VDR recordings (as known
from the DVDArchive-patch for VDR). This plugin extends VDR's '-r'-option with
messages for deleting, moving and renaming a recording.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
VDR_PLUGIN_EXTRA_FLAGS="-DUSE_GRAPHTFT"
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY contrib scripts
