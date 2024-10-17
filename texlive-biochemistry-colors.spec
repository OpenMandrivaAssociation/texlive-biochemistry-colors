Name:		texlive-biochemistry-colors
Version:	54512
Release:	2
Summary:	Colors used to display amino acids, nucleotides, sugars or atoms in biochemistry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biochemistry-colors
License:	lppl gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biochemistry-colors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biochemistry-colors.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Biochemistry-colors.sty defines the standard colors of
biochemistry for use with the color package and the xcolor
package. xcolor is loaded by Biochemistry-colors.sty. Colors
include: Shapely-colors for amino acids and nucleotides.
CPK-Colors (Corey, Pauling and Koltun) of elements. Jmol-colors
of elements, important isotopes and structures. Glycopedia
colors for sugars.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biochemistry-colors
%doc %{_texmfdistdir}/doc/latex/biochemistry-colors

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
