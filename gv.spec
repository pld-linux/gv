Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de):	Verbessertes Frontend f�r Ghostscript
Summary(fr):	Frontal am�lior� pour ghostscript
Summary(pl):	Zaawansowana nak�adka na ghostscripta (interpreter PostScriptu(TM))
Summary(tr):	Ghostscript i�in grafik aray�z
Name:		gv
Version:	3.5.8
Release:	23
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.gz
# Source0-md5:	8f2f0bd97395d6cea52926ddee736da8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-alias.patch
Patch2:		%{name}-quote.patch
Patch3:		%{name}-fix_NoMan.patch
Patch4:		%{name}-wheel.patch
Patch5:		%{name}-buffer.patch
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel >= 1.5E
Requires:	ghostscript
Obsoletes:	ghostview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
gv provides a user interface for the ghostscript PostScript(TM)
interpreter. Derived from the ghostview program, gv can display
PostScript and PDF documents using the X Window System.

%description -l de
gv erm�glicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfl�che f�r den
Ghostscript- Interpreter bereitstellt. gv basiert auf dem �lteren
Programm ghostview.

%description -l fr
gv permet de visualiser et de naviguer dans les documents PostScript
et PDF sur un �cran X en offrant une interface pour l'interpr�teur
ghostscript. gv est bas� sur un ancien programme appel� ghostview.

%description -l pl
gv umo�liwia ogl�danie i manipulacj� plikami postscriptowymi i
dokumentami w formacie PDF pod X Window. Udost�pnia graficzny
interfejs u�ytkownika do programu ghostscript b�d�cego interpreterem
j�zyka postscript.

%description -l tr
gv, PostScript ve PDF dosyalar�n� bir X ekran� �zerinde g�sterebilen
ve �zerlerinde dola�may� sa�layan bir ghostscript aray�z�d�r.
Ghostview ad�yla bilinen programdan yola ��k�larak haz�rlanm��t�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i \
	-e 's|#include[ 	]*INC_X11(\([^)]*\))|#include <X11/\1>|' \
	-e 's|#include[ 	]*INC_XMU(\([^)]*\))|#include <X11/Xmu/\1>|' \
	-e 's|#include[ 	]*INC_XAW(\([^)]*\))|#include <X11/Xaw3d/\1>|' \
	source/*.c source/*.h

%build
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
ln -sf gv $RPM_BUILD_ROOT%{_bindir}/ghostview

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gunzip doc/*gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html README CHANGES doc/*doc doc/*txt
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/gv
%{_appdefsdir}/GV
%{_desktopdir}/gv.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gv.1x*
