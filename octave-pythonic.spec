%global octpkg pythonic
%global debug_package %{nil}

#NOTE: use latest commit because v0-0.1 won't build with octave 8
#global commit 2719316094d59fc75e5b7241c1a7e1e133da8680
%global commit	3dbe9a06c1dec1a138f398b951e18044a00e063d

Summary:	The Pythonic package provides a Python language binding for Octave, to allow an
Name:		octave-pythonic
Version:	0.0.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/pythonic/
Url:		https://gitlab.com/mtmiller/octave-pythonic/
#Source0:	https://gitlab.com/mtmiller/octave-pythonic/-/archive/v%{version}/%{name}-%{version}.tar.bz2
Source0:	https://gitlab.com/mtmiller/octave-pythonic/-/archive/%{commit}/octave-pythonic-%{commit}.tar.bz2

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:  pkgconfig(python)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Pythonic package provides a Python language binding for Octave, 
to allow any Python package to be loaded and used directly, with 
automatic translation from Octave to Python data types.

%files
%license COPYING
%doc NEWS.md README.md
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml


#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?commit:%{commit}}%{!?commit:%{version}-%{commit}}

# remove the '+' char from the version 
sed -i -e 's,^Version: \(.*\)+,Version: \1,' DESCRIPTION

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

