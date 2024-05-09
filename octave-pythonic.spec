%global octpkg pythonic
%global debug_package %{nil}

Summary:	The Pythonic package provides a Python language binding for Octave, to allow an
Name:		octave-pythonic
Version:	0.1.3
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/pythonic/
Url:		https://gitlab.com/mtmiller/octave-pythonic/
Source0:	https://gitlab.com/gnu-octave/octave-%{octpkg}/-/releases/v%{version}/downloads/octave-%{octpkg}-%{version}.tar.gz

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
%autosetup -p1

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

