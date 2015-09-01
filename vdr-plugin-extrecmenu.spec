%define plugin	extrecmenu

Summary:	VDR plugin: Extended recordings menu
Name:		vdr-plugin-%plugin
Version:	1.2.4
Release:	1
Group:		Video
License:	GPL
URL:		http://projects.vdr-developer.org/projects/show/plg-extrecmenu
Source:		http://projects.vdr-developer.org/git/vdr-plugin-extrecmenu.git/snapshot/vdr-plugin-%plugin-%{version}.tar.bz2
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
%setup -q
%vdr_plugin_prep

%build
VDR_PLUGIN_EXTRA_FLAGS="-DUSE_GRAPHTFT"
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY contrib scripts


