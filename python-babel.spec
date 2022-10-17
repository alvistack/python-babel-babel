# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-babel
Epoch: 100
Version: 2.10.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Internationalization utilities
License: BSD-3-Clause
URL: https://github.com/python-babel/babel/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A collection of tools for internationalizing Python applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-Babel
Summary: Internationalization utilities
Requires: python3
Requires: python3-pytz >= 2015.7
Provides: python3-babel = %{epoch}:%{version}-%{release}
Provides: python3dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(babel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Babel
A collection of tools for internationalizing Python applications.

%files -n python%{python3_version_nodots}-Babel
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-Babel
Summary: Internationalization utilities
Requires: python3
Requires: python3-pytz >= 2015.7
Provides: python3-babel = %{epoch}:%{version}-%{release}
Provides: python3dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(babel) = %{epoch}:%{version}-%{release}

%description -n python3-Babel
A collection of tools for internationalizing Python applications.

%files -n python3-Babel
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-babel
Summary: Internationalization utilities
Requires: python3
Requires: python3-pytz >= 2015.7
Provides: python3-babel = %{epoch}:%{version}-%{release}
Provides: python3dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(babel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-babel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(babel) = %{epoch}:%{version}-%{release}

%description -n python3-babel
A collection of tools for internationalizing Python applications.

%files -n python3-babel
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
