Summary:	Enhanced frontend for ghostscript
Summary(de):	Verbessertes Frontend für Ghostscript 
Summary(fr):	Frontal amélioré pour ghostscript
Summary(pl):	Zaawansowana nak³adka na ghostscript'a
Summary(tr):	Ghostscript için grafik arayüz
Name:		gv
Version:	3.5.8
Release:	8
Copyright:	GPL
Group:		X11/Applications/Graphics
Requires:	ghostscript
Source0:	ftp://thep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.gz
Source1:	gv.desktop
Patch0:		gv-config.patch
Patch1:		gv-alias.patch
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
Obsoletes:	ghostview
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

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
%patch0 -p1
%patch1 -p1

%build
xmkmf
make Makefiles
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/applnk/Applications

make install install.man DESTDIR=$RPM_BUILD_ROOT
ln -sf gv $RPM_BUILD_ROOT%{_bindir}/ghostview

mv -f $RPM_BUILD_ROOT/%{_libdir}/X11/gv/gv_class.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/GV
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Applications

gunzip doc/*gz
gzip -9nf README CHANGES doc/*doc doc/*txt \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html {README,CHANGES,doc/*doc,doc/*txt}.gz
/etc/X11/applnk/Applications/gv.desktop
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/GV
%{_mandir}/man1/gv.1x*
