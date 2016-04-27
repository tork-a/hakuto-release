Name:           ros-jade-tetris-gazebo
Version:        0.1.8
Release:        0%{?dist}
Summary:        ROS tetris_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/tetris_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-gazebo-plugins
Requires:       ros-jade-gazebo-ros
Requires:       ros-jade-gazebo-ros-control
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-rosbash
Requires:       ros-jade-tetris-description
Requires:       ros-jade-xacro
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-gazebo-plugins

%description
This package contains specific ROS simulation setting for hakuto robots. Note:
&quot;models&quot; directory is temporary and should be removed once this
pullrequest to gazebo_model gets merged.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Apr 27 2016 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.8-0
- Autogenerated by Bloom

* Wed Apr 27 2016 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.7-0
- Autogenerated by Bloom

* Wed Apr 27 2016 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.6-0
- Autogenerated by Bloom

* Wed Apr 27 2016 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.5-0
- Autogenerated by Bloom

