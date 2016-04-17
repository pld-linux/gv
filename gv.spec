#
# Conditional build:
%bcond_with	libzio	# use libzio for I/O (currently doesn't work because of unsupported seeking)
#
Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de.UTF-8):	Verbessertes Frontend für Ghostscript
Summary(fr.UTF-8):	Frontal amélioré pour ghostscript
Summary(pl.UTF-8):	Zaawansowana nakładka na ghostscripta (interpreter PostScriptu(TM))
Summary(tr.UTF-8):	Ghostscript için grafik arayüz
Name:		gv
Version:	3.7.4
Release:	2
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/gv/%{name}-%{version}.tar.gz
# Source0-md5:	80035c43285781b68361acda09ad7441
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-wheel.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-am.patch
URL:		http://www.gnu.org/software/gv/ 
BuildRequires:	Xaw3d-devel >= 1.5E
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_libzio:BuildRequires:	libzio-devel}
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
Requires:	ghostscript-x11
Obsoletes:	ghostview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gv provides a user interface for the ghostscript PostScript(TM)
interpreter. Derived from the ghostview program, gv can display
PostScript and PDF documents using the X Window System.

%description -l de.UTF-8
gv ermöglicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfläche für den
Ghostscript- Interpreter bereitstellt. gv basiert auf dem älteren
Programm ghostview.

%description -l fr.UTF-8
gv permet de visualiser et de naviguer dans les documents PostScript
et PDF sur un écran X en offrant une interface pour l'interpréteur
ghostscript. gv est basé sur un ancien programme appelé ghostview.

%description -l pl.UTF-8
gv umożliwia oglądanie i manipulację plikami postscriptowymi i
dokumentami w formacie PDF pod X Window. Udostępnia graficzny
interfejs użytkownika do programu ghostscript będącego interpreterem
języka postscript.

%description -l tr.UTF-8
gv, PostScript ve PDF dosyalarını bir X ekranı üzerinde gösterebilen
ve üzerlerinde dolaşmayı sağlayan bir ghostscript arayüzüdür.
Ghostview adıyla bilinen programdan yola çıkılarak hazırlanmıştır.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# libzio uses weak symbols to access libbz2 and libz, so -as-needed
# normally kills them from linking
%{?with_libzio:LDFLAGS="-lbz2 -lz %{rpmldflags}"}
%configure \
	%{!?with_libzio:ac_cv_header_zlib_h=no ac_cv_header_bzlib_h=no ac_cv_header_zio_h=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
ln -sf gv $RPM_BUILD_ROOT%{_bindir}/ghostview

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ghostview
%attr(755,root,root) %{_bindir}/gv
%attr(755,root,root) %{_bindir}/gv-update-userconfig
%{_datadir}/gv
%{_desktopdir}/gv.desktop
%{_pixmapsdir}/gv.png
%{_mandir}/man1/gv.1*
%{_mandir}/man1/gv-update-userconfig.1*
%{_infodir}/gv.info*
