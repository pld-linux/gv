Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de):	Verbessertes Frontend f�r Ghostscript 
Summary(fr):	Frontal am�lior� pour ghostscript
Summary(pl):	Zaawansowana nak�adka na ghostscript'a (interpreter PostScriptu(TM))
Summary(tr):	Ghostscript i�in grafik aray�z
Name:		gv
Version:	3.5.8
Release:	9
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
Source0:	ftp://thep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.gz
Source1:	gv.desktop
Patch0:		gv-config.patch
Patch1:		gv-alias.patch
Requires:	ghostscript
Obsoletes:	ghostview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gv provides a user interface for the ghostscript PostScript(TM) interpreter. 
Derived from the ghostview program, gv can display PostScript and PDF
documents using the X Window System.

%description -l de
gv erm�glicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfl�che f�r den Ghostscript-
Interpreter bereitstellt. gv basiert auf dem �lteren Programm ghostview.

%description -l fr
gv permet de visualiser et de naviguer dans les documents PostScript et PDF
sur un �cran X en offrant une interface pour l'interpr�teur ghostscript. gv
est bas� sur un ancien programme appel� ghostview.

%description -l pl
gv umo�liwia ogl�danie i manipulacj� plikami postscriptowymi i dokumentami w
formacie PDF pod X Window. Udost�pnia graficzny interfejs u�ytkownika do
programu ghostscript b�d�cego interpreterem j�zyka postscript.

%description -l tr
gv, PostScript ve PDF dosyalar�n� bir X ekran� �zerinde g�sterebilen ve
�zerlerinde dola�may� sa�layan bir ghostscript aray�z�d�r. Ghostview ad�yla
bilinen programdan yola ��k�larak haz�rlanm��t�r.

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
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Applications

make install install.man DESTDIR=$RPM_BUILD_ROOT
ln -sf gv $RPM_BUILD_ROOT%{_bindir}/ghostview

mv -f $RPM_BUILD_ROOT/%{_libdir}/X11/gv/gv_class.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/GV
install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Applications

gunzip doc/*gz
gzip -9nf README CHANGES doc/*doc doc/*txt \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html {README,CHANGES,doc/*doc,doc/*txt}.gz
/usr/X11R6/share/applnk/Applications/gv.desktop
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/GV
%{_mandir}/man1/gv.1x*
