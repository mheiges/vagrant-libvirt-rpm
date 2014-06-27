# Based on the spec file that was generated from 
# vagrant-libvirt-0.0.18.gem by gem2rpm -*- rpm-spec -*-
%global gem_name vagrant-libvirt

Name: rubygem-%{gem_name}
Version: 0.0.16
Release: 1%{?dist}
Summary: Vagrant provider for libvirt
Group: Development/Languages
License: MIT
URL: https://github.com/pradels/vagrant-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(fog) => 1.15
Requires: rubygem(fog) < 2
Requires: rubygem(ruby-libvirt) => 0.4.0
Requires: rubygem(ruby-libvirt) < 0.5
#Requires: rubygem(nokogiri) => 1.5.9
#Requires: rubygem(nokogiri) < 1.6
Requires: rubygem(nokogiri)
Requires: rubygem(multi_json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Vagrant provider for libvirt.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}

%doc %dir %{gem_instdir}/example_box
%doc %{gem_instdir}/example_box

%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/vagrant-libvirt.gemspec

%dir %{gem_instdir}/locales
%{gem_instdir}/locales

%dir %{gem_instdir}/tools
%{gem_instdir}/tools

%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Fri Jun 27 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.16-1
- Initial package for Fedora