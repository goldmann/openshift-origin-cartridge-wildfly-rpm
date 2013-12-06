%global cartridgedir %{_libexecdir}/openshift/cartridges/wildfly
%global namedreltag .Beta1.1
%global namedversion %{version}%{?namedreltag}

Summary:       Provides WildFly support
Name:          openshift-origin-cartridge-wildfly
Version:       8.0.0
Release:       0.1%{namedreltag}%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       https://github.com/goldmann/openshift-origin-cartridge-wildfly/archive/%{namedversion}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
Requires:      facter
Requires:      bc
Requires:      maven
Requires:      wildfly

BuildArch:     noarch

%description
Provides WildFly support to OpenShift. (Cartridge Format V2)

%prep
%setup -q -n openshift-origin-cartridge-wildfly-%{version}-%{reltag}%{namedreltag}

%install
mkdir -p %{buildroot}%{cartridgedir}/info
cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%dir %{cartridgedir}/info
%{cartridgedir}/bin
%{cartridgedir}/versions/8
%{cartridgedir}/hooks
%{cartridgedir}/env
%{cartridgedir}/metadata
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Fri Dec 06 2013 Marek Goldmann <mgoldman@redhat.com> - 8.0.0-0.1.Beta1.1
- Initial packaging

