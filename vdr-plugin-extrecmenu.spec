
%define plugin	extrecmenu
%define name	vdr-plugin-%plugin
%define version	1.1
%define rel	6

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


%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 1.1-6mdv2011.0
+ Revision: 404568
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.1-5mdv2010.0
+ Revision: 402765
- add graphtft support (graphtft.patch)

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.1-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- fix build with gcc4.4 (const-char-gcc4.4.patch)

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.1-3mdv2009.1
+ Revision: 359316
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.1-2mdv2009.0
+ Revision: 197928
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.1-1mdv2009.0
+ Revision: 197668
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.13-6mdv2008.1
+ Revision: 145094
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.13-5mdv2008.1
+ Revision: 103093
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.13-4mdv2008.0
+ Revision: 49999
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.13-3mdv2008.0
+ Revision: 42085
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.13-2mdv2008.0
+ Revision: 22756
- rebuild for new vdr


* Fri Mar 02 2007 Anssi Hannula <anssi@mandriva.org> 0.13-1mdv2007.0
+ Revision: 130880
- 0.13

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-7mdv2007.1
+ Revision: 90920
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-6mdv2007.1
+ Revision: 74007
- rebuild for new vdr
- Import vdr-plugin-extrecmenu

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-2mdv2007.0
- rebuild for new vdr

* Tue Jul 11 2006 Anssi Hannula <anssi@mandriva.org> 0.12a-1mdv2007.0
- initial Mandriva release

