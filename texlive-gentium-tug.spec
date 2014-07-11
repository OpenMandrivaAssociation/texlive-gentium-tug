# revision 31194
# category Package
# catalog-ctan /fonts/gentium-tug
# catalog-date 2013-07-10 10:52:50 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-gentium-tug
Version:	1.0
Release:	7
Summary:	Gentium fonts (in two formats) and support files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gentium-tug
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium-tug.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GenBasB.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GenBasBI.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GentiumPlus-I.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GentiumPlus-R.afm
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-agr.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-ttf-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-ttf.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-l7x-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ot1-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-qx-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2a-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2b-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2c-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5-ttf.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-texnansi-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-x2-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-x2.enc
%{_texmfdistdir}/fonts/map/dvips/gentium-tug/gentium-type1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-agr.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ec.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-l7x.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-lgr.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ot1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-qx.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2a.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2b.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2c.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t5.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-texnansi.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-truetype.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ts1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-x2.map
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/agr-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/agr-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/lgr-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/lgr-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasB.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasBI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasR.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasB.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasBI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasR.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/Gentium-I.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/Gentium-R.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumAlt-I.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumAlt-R.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlus-I.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlus-R.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlusCompact-I.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlusCompact-R.ttf
%{_texmfdistdir}/fonts/type1/public/gentium-tug/GenBasB.pfb
%{_texmfdistdir}/fonts/type1/public/gentium-tug/GenBasBI.pfb
%{_texmfdistdir}/fonts/type1/public/gentium-tug/GentiumPlus-I.pfb
%{_texmfdistdir}/fonts/type1/public/gentium-tug/GentiumPlus-R.pfb
%{_texmfdistdir}/tex/context/third/gentium-tug/type-gentium.mkii
%{_texmfdistdir}/tex/context/third/gentium-tug/type-gentium.mkiv
%{_texmfdistdir}/tex/latex/gentium-tug/gentium.sty
%{_texmfdistdir}/tex/latex/gentium-tug/l7xgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/lgrgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ly1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ot1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/qxgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2agentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2bgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2cgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t5gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ts1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/x2gentium.fd
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/GENTIUM-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/QUOTES.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/README.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/GENTIUM-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/GENTIUM-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/README.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/DOCUMENTATION.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/GentiumPlus-features.odt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/GentiumPlus-features.pdf
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/README.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/feat_set_tuned.xml
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/Makefile
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/README
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/gentium.pdf
%doc %{_texmfdistdir}/doc/fonts/gentium-tug/gentium.tex
#- source
%doc %{_texmfdistdir}/source/fonts/gentium-tug/generate-support-files.rb
%doc %{_texmfdistdir}/source/fonts/gentium-tug/gentium.rb
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/README
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-agr.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-lgr.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-t2a.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-t2b.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-t2c.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/lig/gentium-x2.lig
%doc %{_texmfdistdir}/source/fonts/gentium-tug/make-zip-4CTAN.sh
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/GentiumPlus-I-Czech.kern
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/GentiumPlus-R-Czech.kern
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/Makefile
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/afmcreator.py
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/ff-gentium.pe
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/generate-extra-kerns.sh
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/greekcorrection.py
%doc %{_texmfdistdir}/source/fonts/gentium-tug/type1/kerncorrection.py

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
