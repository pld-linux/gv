Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de):	Verbessertes Frontend für Ghostscript
Summary(fr):	Frontal amélioré pour ghostscript
Summary(pl):	Zaawansowana nak³adka na ghostscript'a (interpreter PostScriptu(TM))
Summary(tr):	Ghostscript için grafik arayüz
Name:		gv
Version:	3.5.8
Release:	19
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-alias.patch
Patch2:		%{name}-quote.patch
Patch3:		%{name}-fix_NoMan.patch
Patch4:		%{name}-wheel.patch
Patch5:		%{name}-buffer.patch
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
BuildRequires:	Xaw3d-devel >= 1.5
BuildRequires:	XFree86-devel
Requires:	ghostscript
Obsoletes:	ghostview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gv provides a user interface for the ghostscript PostScript(TM)
interpreter. Derived from the ghostview program, gv can display
PostScript and PDF documents using the X Window System.

%description -l de
gv ermöglicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfläche für den
Ghostscript- Interpreter bereitstellt. gv basiert auf dem älteren
Programm ghostview.

%description -l fr
gv permet de visualiser et de naviguer dans les documents PostScript
et PDF sur un écran X en offrant une interface pour l'interpréteur
ghostscript. gv est basé sur un ancien programme appelé ghostview.

%description -l pl
gv umo¿liwia ogl±danie i manipulacjê plikami postscriptowymi i
dokumentami w formacie PDF pod X Window. Udostêpnia graficzny
interfejs u¿ytkownika do programu ghostscript bêd±cego interpreterem
jêzyka postscript.

%description -l tr
gv, PostScript ve PDF dosyalarýný bir X ekraný üzerinde gösterebilen
ve üzerlerinde dolaþmayý saðlayan bir ghostscript arayüzüdür.
Ghostview adýyla bilinen programdan yola çýkýlarak hazýrlanmýþtýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_datadir}/pixmaps}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
ln -sf gv $RPM_BUILD_ROOT%{_bindir}/ghostview

mv -f $RPM_BUILD_ROOT/%{_libdir}/X11/gv/gv_class.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/GV

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gunzip doc/*gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html README CHANGES doc/*doc doc/*txt
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/Viewers/gv.desktop
%{_pixmapsdir}/*
%{_libdir}/X11/app-defaults/GV
%{_mandir}/man1/gv.1x*
