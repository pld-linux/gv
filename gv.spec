Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de.UTF-8):	Verbessertes Frontend für Ghostscript
Summary(fr.UTF-8):	Frontal amélioré pour ghostscript
Summary(pl.UTF-8):	Zaawansowana nakładka na ghostscripta (interpreter PostScriptu(TM))
Summary(tr.UTF-8):	Ghostscript için grafik arayüz
Name:		gv
Version:	3.6.4
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/gv/%{name}-%{version}.tar.gz
# Source0-md5:	34ea686ea499c938e152ab424859b903
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-buffer.patch
Patch1:		%{name}-quote.patch
Patch2:		%{name}-wheel.patch
Patch3:		%{name}-info.patch
URL:		http://www.gnu.org/software/gv/ 
BuildRequires:	Xaw3d-devel >= 1.5E
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libXmu-devel
Requires:	ghostscript
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
%patch3 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%{_libdir}/gv
%{_desktopdir}/gv.desktop
%{_pixmapsdir}/gv.png
%{_mandir}/man1/gv.1*
%{_infodir}/gv.info*
