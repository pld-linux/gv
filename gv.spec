Summary:     Enhanced frontend for ghostscript
Summary(de): Verbessertes Frontend für Ghostscript 
Summary(fr): Frontal amélioré pour ghostscript
Summary(pl): Zaawansowana nak³adka na ghostscript'a
Summary(tr): Ghostscript için grafik arayüz
Name:        gv
Version:     3.5.8
Release:     6
Copyright:   GPL
Group:       X11/Applications/Graphics
Requires:    ghostscript
Source0:     ftp://thep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.gz
Source1:     gv.wmconfig
Patch0:      gv-3.5.8-config.patch
URL:         http://wwwthep.physik.uni-mainz.de/~plass/gv/
Obsoletes:   ghostview
BuildRoot:	/tmp/%{name}-%{version}-root

%description
gv allows to view and navigate through PostScript and PDF documents on an X
display by providing a user interface for the ghostscript interpreter.  gv
is based upon an earlier program known as ghostview.

%description -l de
gv ermöglicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfläche für den Ghostscript-
Interpreter bereitstellt. gv basiert auf dem älteren Programm ghostview.

%description -l fr
gv permet de visualiser et de naviguer dans les documents PostScript et PDF
sur un écran X en offrant une interface pour l'interpréteur ghostscript. gv
est basé sur un ancien programme appelé ghostview.

%description -l pl
gv umo¿liwia ogl±danie i manipulacjê plikami postscriptowymi i dokumentami w
formacie PDF pod X Window. Udostêpnia graficzny interfejs u¿ytkownika do
programu ghostscript bêd±cego jednym z interpreterów jezyka postscript.
Wywodzi sie od programu ghostview.

%description -l tr
gv, PostScript ve PDF dosyalarýný bir X ekraný üzerinde gösterebilen ve
üzerlerinde dolaþmayý saðlayan bir ghostscript arayüzüdür. Ghostview adýyla
bilinen programdan yola çýkýlarak hazýrlanmýþtýr.

%prep
%setup -q
%patch0 -p1 -b .config

%build
xmkmf
make Makefiles
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install install.man DESTDIR=$RPM_BUILD_ROOT
gunzip doc/*gz
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/gv
ln -sf gv $RPM_BUILD_ROOT/usr/X11R6/bin/ghostview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*.html doc/*doc doc/*txt
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/lib/X11/gv
%config /usr/X11R6/lib/X11/app-defaults/GV
/usr/X11R6/man/man1/gv.1x
/etc/X11/wmconfig/gv
