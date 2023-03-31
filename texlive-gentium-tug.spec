Name:		texlive-gentium-tug
Version:	63470
Release:	2
Summary:	Gentium fonts (in two formats) and support files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gentium-tug
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Gentium is a typeface family designed to enable the diverse
ethnic groups around the world who use the Latin, Cyrillic and
Greek scripts to produce readable, high-quality publications.
It supports a wide range of Latin- and Cyrillic-based
alphabets. The package consists of: - The original (unaltered)
GentiumPlus, GentiumBook, and other Gentium-family fonts in
TrueType format, as developed by SIL and released under the OFL
(see OFL.txt and OFL-FAQ.txt); - Converted fonts in PostScript
Type 1 format, released under the same terms. These incorporate
the name "Gentium" by permission of SIL given to the TeX Users
Group; - ConTeXt, LaTeX and other supporting files; - TeX-
related documentation, and the SIL documentation and other
files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gentium-tug
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug
%{_texmfdistdir}/fonts/map/dvips/gentium-tug
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug
%{_texmfdistdir}/fonts/tfm/public/gentium-tug
%{_texmfdistdir}/fonts/truetype/public/gentium-tug
%{_texmfdistdir}/fonts/type1/public/gentium-tug
%{_texmfdistdir}/tex/latex/gentium-tug
%doc %{_texmfdistdir}/doc/fonts/gentium-tug
#- source
%doc %{_texmfdistdir}/source/fonts/gentium-tug

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
