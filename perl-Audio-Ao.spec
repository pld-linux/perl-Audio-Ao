#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	Ao
Summary:	Audio::Ao - wrapper for the Ao audio library
Summary(pl):	Audio::Ao - wrapper dla biblioteki d¼wiêkowej Ao
Name:		perl-Audio-Ao
Version:	0.01
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37b1c67199c90aff616d4c1fff381d61
BuildRequires:	libao-devel
%if %{with tests}
BuildRequires:	perl-Inline-C
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Inline-C
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides access to Libao, "a cross-platform library that allows
programs to output PCM audio data to the native audio devices on a
wide variety of platforms.". Libao currently supports OSS, ESD, ALSA,
Sun audio, and aRts.

%description -l pl
Modu³ daje dostêp do Libao - "wieloplatformowej biblioteki
pozwalaj±cej programom odtwarzaæ dane d¼wiêkowe PCM na urz±dzeniach
d¼wiêkowych natywnych dla wielu platform". Libao aktualnie obs³uguje
d¼wiêk OSS, ESD, ALSA, Sun audio i aRts.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Audio/Ao/Ao.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Ao/Ao.so
%{_mandir}/man3/*
