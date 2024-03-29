#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Audio
%define		pnam	Ao
Summary:	Audio::Ao - wrapper for the Ao audio library
Summary(pl.UTF-8):	Audio::Ao - wrapper dla biblioteki dźwiękowej Ao
Name:		perl-Audio-Ao
Version:	0.01
Release:	5
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37b1c67199c90aff616d4c1fff381d61
Patch0:		%{name}-fix.patch
URL:		http://search.cpan.org/dist/Audio-Ao/
BuildRequires:	libao-devel
%if %{with tests}
BuildRequires:	perl-Inline-C
%endif
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Inline-C
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides access to Libao, "a cross-platform library that allows
programs to output PCM audio data to the native audio devices on a
wide variety of platforms.". Libao currently supports OSS, ESD, ALSA,
Sun audio, and aRts.

%description -l pl.UTF-8
Moduł daje dostęp do Libao - "wieloplatformowej biblioteki
pozwalającej programom odtwarzać dane dźwiękowe PCM na urządzeniach
dźwiękowych natywnych dla wielu platform". Libao aktualnie obsługuje
dźwięk OSS, ESD, ALSA, Sun audio i aRts.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Audio/Ao.pm
%dir %{perl_vendorarch}/auto/Audio/Ao
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Ao/Ao.so
%{_mandir}/man3/*
