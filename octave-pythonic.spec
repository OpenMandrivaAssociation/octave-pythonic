%define octpkg pythonic

%global commit 2719316094d59fc75e5b7241c1a7e1e133da8680

Summary:	A python  binding for GNU Octave
Name:		octave-%{octpkg}
Version:	0.0.1
Release:	1
Url:		https://gitlab.com/mtmiller/%{name}
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Sciences/Mathematics
#BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Pythonic is a package that provides a Python native calling interface for
GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}-%{commit}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
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

