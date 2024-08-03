# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate quanta

Name:           rust-quanta
Version:        0.12.3
Release:        %autorelease
Summary:        High-speed timing library

License:        MIT
URL:            https://crates.io/crates/quanta
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          quanta-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
High-speed timing library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+flaky_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flaky_tests-devel %{_description}

This package contains library source intended for building other packages which
use the "flaky_tests" feature of the "%{crate}" crate.

%files       -n %{name}+flaky_tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prost-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prost-devel %{_description}

This package contains library source intended for building other packages which
use the "prost" feature of the "%{crate}" crate.

%files       -n %{name}+prost-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prost-types-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prost-types-devel %{_description}

This package contains library source intended for building other packages which
use the "prost-types" feature of the "%{crate}" crate.

%files       -n %{name}+prost-types-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
