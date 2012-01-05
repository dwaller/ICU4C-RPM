# ICU4C as an RPM for RHEL6 #

The ICU [download page](http://site.icu-project.org/download) provides binary
downloads for Red Hat, but only as tgz files that need to be unpacked into `/`.
You end up with files all over your filesystem, and no way to remove them in a
controlled fashion if you want to upgrade to a later version of ICU.

Exactly the problem RPMs were designed to solve - so I've created an RPM spec
file for the current (5 Jan 2012) version of ICU4C (4.8.1.1) and produced an RPM
from it.

## To update the RPM ##

 - [Download](http://site.icu-project.org/download) the latest version of
   ICU4C.
 - Put the tgz in `~/rpmbuild/SOURCES` (if this doesn't exist, run
   `rpmdev-setuptree`).
 - Put the spec file from this repository in `~/rpmbuild/SPECS`.
 - Update the icu4c.spec Version and Release fields.
 - From that SPECS directory run `rpmbuild -bb icu4c.spec`
 - If you get any warnings about missing or extraneous files you may need to
   update the icu4c.spec to include/exclude these files.  If there are many
   changes you might want to get a list of files (not directories) in the tgz:
   `tar xf icu4c-...RHEL6-x64.tgz && find usr -not -type d`

