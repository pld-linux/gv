Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Summary(de.UTF-8):	Verbessertes Frontend für Ghostscript
Summary(fr.UTF-8):	Frontal amélioré pour ghostscript
Summary(pl.UTF-8):	Zaawansowana nakładka na ghostscripta (interpreter PostScriptu(TM))
Summary(tr.UTF-8):	Ghostscript için grafik arayüz
Name:		gv
Version:	3.6.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnu.org/gnu/gv/%{name}-%{version}.tar.gz
# Source0-md5:	dcdb2205cf0c61394419e015c7548df1
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-buffer.patch
Patch1:		%{name}-quote.patch
Patch2:		%{name}-wheel.patch
Patch3:		%{name}-info.patch
URL:		http://wwwthep.physik.uni-mainz.de/~plass/gv/
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
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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
%{_mandir}/man1/gv.1*
%{_infodir}/gv.info*
