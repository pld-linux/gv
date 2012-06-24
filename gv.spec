Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de):	Verbessertes Frontend f�r Ghostscript
Summary(fr):	Frontal am�lior� pour ghostscript
Summary(pl):	Zaawansowana nak�adka na ghostscripta (interpreter PostScriptu(TM))
Summary(tr):	Ghostscript i�in grafik aray�z
Name:		gv
Version:	3.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnu.org/gnu/gv/%{name}-%{version}.tar.gz
# Source0-md5:	c1b26aae6890f3a6a787a55d8284c21b
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel >= 1.5E
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo
Requires:	ghostscript
Obsoletes:	ghostview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gv
%{_desktopdir}/gv.desktop
%{_pixmapsdir}/*
%{_infodir}/gv.*
