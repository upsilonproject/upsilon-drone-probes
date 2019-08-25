%include SPECS/.buildid.rpmmacro

Name:		upsilon-drone-probes
Version:	%{version_formatted_short}
Release:	%{timestamp}.%{?dist}
Summary:	Monitoring software
BuildArch: 	noarch

Group:		Applications/System
License:	GPLv2
URL:		http://upsilon-project.co.uk
Source0:	upsilon-drone-probes.zip

BuildRequires:	python
Requires:	python upsilon-pycommon

Obsoletes: upsilon-serviceChecks
Provides: upsilon-serviceChecks
Conflicts: upsilon-serviceChecks

%description
Monitoring software

%prep
rm -rf $RPM_BUILD_DIR/*
%setup -q -n upsilon-drone-probes

%build
mkdir -p %{buildroot}/usr/sbin
cp src/* %{buildroot}/usr/sbin/

%files
/usr/sbin/*

%changelog
* Sun Aug 25 2019 James Read <contact@jread.com> 2.0.0
	Rename from serviceChecks

* Mon Jun 06 2016 James Read <contact@jwread.com> 1.0.0-1
	Initial version.

