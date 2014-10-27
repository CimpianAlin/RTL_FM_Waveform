# RPM package for RTL_FM_Waveform
# This file is regularly AUTO-GENERATED by the IDE. DO NOT MODIFY.

# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

Name: RTL_FM_Waveform
Summary: Waveform RTL_FM_Waveform
Version: 1.0.0
Release: 1
License: None
Group: REDHAWK/Waveforms
Source: %{name}-%{version}.tar.gz
# Require the controller whose SPD is referenced
Requires: RTL_FM_Controller
# Require each referenced component
Requires: TuneFilterDecimate RTL_FM_Controller AmFmPmBasebandDemod NOOP psd fastfilter ArbitraryRateResampler VorbisEncoder DataConverter
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description

%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dom/waveforms/%{name}"
%__install -m 644 RTL_FM_Waveform.sad.xml $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/%{name}/RTL_FM_Waveform.sad.xml

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/waveforms/%{name}
%{_prefix}/dom/waveforms/%{name}/RTL_FM_Waveform.sad.xml
